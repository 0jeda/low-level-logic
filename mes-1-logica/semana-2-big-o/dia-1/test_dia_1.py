#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

def float_cercano(val1, val2, epsilon=1e-3):
    try: return abs(float(val1) - float(val2)) <= epsilon
    except ValueError: return False

def validar_reto38(salida, suma_esp, prom_esp):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 2:
        return False, f"Se esperaban 2 líneas, se recibieron {len(lineas)}."
    dict_salida = {}
    for l in lineas:
        if '=' not in l: return False, f"Formato incorrecto: {l}"
        k, v = l.split('=', 1)
        dict_salida[k.upper()] = v.strip()
    
    if "SUMA" not in dict_salida or "PROMEDIO" not in dict_salida:
        return False, "Faltan claves SUMA o PROMEDIO."
    
    try:
        s_obtenida = int(dict_salida["SUMA"])
        if s_obtenida != suma_esp:
            return False, f"Suma incorrecta. Esperada: {suma_esp}, Obtenida: {s_obtenida}"
    except ValueError:
        return False, f"Suma debe ser entera. Obtenido: {dict_salida['SUMA']}"
        
    if not float_cercano(dict_salida["PROMEDIO"], prom_esp):
        return False, f"Promedio incorrecto. Esperado cercano a: {prom_esp}, Obtenido: {dict_salida['PROMEDIO']}"
        
    return True, ""

TEST_CASES = {
    36: [
        ("5\n10 20 30 40 50\n2\n", ["VALOR=30", "OFFSET=8"], "Índice 2 (en rango)"),
        ("3\n1 2 3\n0\n", ["VALOR=1", "OFFSET=0"], "Índice 0 (dirección base)"),
        ("5\n1 2 3 4 5\n5\n", ["ERROR"], "Índice 5 (fuera de límites superior)"),
        ("5\n1 2 3 4 5\n-1\n", ["ERROR"], "Índice -1 (fuera de límites inferior)"),
    ],
    37: [
        ("5\n10 2 30 -5 18\n", ["MAX=30", "MIN=-5"], "Elementos positivos, negativos y desordenados"),
        ("1\n42\n", ["MAX=42", "MIN=42"], "Un único elemento"),
        ("4\n-1 -2 -3 -4\n", ["MAX=-1", "MIN=-4"], "Todos los elementos negativos"),
    ],
    38: [
        ("5\n1 2 3 4 5\n", (15, 3.0), "Suma de 1 a 5"),
        ("0\n", (0, 0.0), "Arreglo vacío (N=0)"),
        ("4\n2 2 3 3\n", (10, 2.5), "Promedio con decimal (.5)"),
    ],
    39: [
        ("5\n1 2 3 4 5\n", ["ARREGLO=5 4 3 2 1"], "Inversión de tamaño impar"),
        ("1\n42\n", ["ARREGLO=42"], "Tamaño 1"),
        ("6\n10 20 30 40 50 60\n", ["ARREGLO=60 50 40 30 20 10"], "Inversión de tamaño par"),
    ],
    40: [
        ("5\n1 2 3 4 5\n", ["ORDENADO=SI"], "Ordenado estrictamente ascendente"),
        ("5\n1 3 2 4 5\n", ["ORDENADO=NO"], "Un desorden en medio"),
        ("1\n42\n", ["ORDENADO=SI"], "Un solo elemento (ordenado trivialmente)"),
        ("3\n5 5 5\n", ["ORDENADO=SI"], "Elementos repetidos (no decreciente)"),
    ]
}

def compilar(ruta_cpp: str) -> str:
    fd, ruta_bin = tempfile.mkstemp(prefix="test_reto_", suffix="")
    os.close(fd)
    res = subprocess.run(["g++", "-O2", "-o", ruta_bin, ruta_cpp], capture_output=True, text=True)
    if res.returncode != 0:
        print("❌ Error de compilación:")
        print(res.stderr)
        try: os.unlink(ruta_bin)
        except OSError: pass
        sys.exit(1)
    return ruta_bin

def ejecutar_caso(ruta_bin: str, entrada: str) -> str:
    res = subprocess.run([ruta_bin], input=entrada, capture_output=True, text=True, timeout=3)
    return res.stdout.strip()

def validar(salida: str, esperados: list) -> bool:
    lineas_salida = [linea.strip() for linea in salida.splitlines() if linea.strip()]
    if len(lineas_salida) != len(esperados):
        print(f"      [ERROR] Se esperaban {len(esperados)} líneas de salida, se recibieron {len(lineas_salida)}.")
        print(f"              Salida recibida:\n{salida}")
        return False
    for idx, (obtenida, esperada) in enumerate(zip(lineas_salida, esperados)):
        if obtenida != esperada:
            print(f"      [ERROR] Línea {idx + 1} incorrecta.")
            print(f"              Esperada: {esperada}")
            print(f"              Obtenida: {obtenida}")
            return False
    return True

def probar_reto(reto_num: int, ruta_cpp: str) -> bool:
    print(f"🔨 Probando Reto {reto_num} con: {ruta_cpp}")
    if not os.path.exists(ruta_cpp):
        print(f"❌ Archivo no encontrado: {ruta_cpp}")
        return False

    ruta_bin = compilar(ruta_cpp)
    exitos = 0
    casos = TEST_CASES[reto_num]
    
    try:
        for idx, (entrada, esperado, desc) in enumerate(casos, 1):
            try:
                salida = ejecutar_caso(ruta_bin, entrada)
                if reto_num == 38:
                    s_esp, p_esp = esperado
                    ok, err = validar_reto38(salida, s_esp, p_esp)
                    if ok:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. {err}")
                else:
                    if validar(salida, esperado):
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}")
            except subprocess.TimeoutExpired:
                print(f"  [TIMEOUT] Caso {idx}: {desc}")
            except Exception as e:
                print(f"  [ERROR] Caso {idx}: {desc} ({e})")
    finally:
        try: os.unlink(ruta_bin)
        except OSError: pass

    total = len(casos)
    if exitos == total:
        print(f"✅ Reto {reto_num}: ¡Pasaron todos los casos ({exitos}/{total})!\n")
        return True
    else:
        print(f"❌ Reto {reto_num}: Fallaron {total - exitos} de {total} casos.\n")
        return False

def detectar_reto(ruta: str) -> int:
    match = re.search(r'reto_?(\d+)', os.path.basename(ruta))
    if match: return int(match.group(1))
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 test_dia_1.py <ruta_cpp> | all")
        sys.exit(1)

    if sys.argv[1].lower() == "all":
        exito_total = True
        base_dir = os.path.dirname(os.path.abspath(__file__))
        soluciones_dir = os.path.join(base_dir, "soluciones")
        
        retos_probados = 0
        for r in sorted(TEST_CASES.keys()):
            posibles_nombres = [f"reto_{r}.cpp", f"reto{r}.cpp"]
            encontrado = False
            for nom in posibles_nombres:
                ruta = os.path.join(soluciones_dir, nom)
                if os.path.exists(ruta):
                    retos_probados += 1
                    if not probar_reto(r, ruta):
                        exito_total = False
                    encontrado = True
                    break

        if retos_probados == 0:
            print("ℹ️ No se encontraron soluciones para probar en soluciones/.")
            sys.exit(0)

        sys.exit(0 if exito_total else 1)

    if len(sys.argv) == 3:
        reto_num = int(sys.argv[1])
        ruta_cpp = sys.argv[2]
    else:
        ruta_cpp = sys.argv[1]
        reto_num = detectar_reto(ruta_cpp)
        if not reto_num:
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_1.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 1 de la Semana 2.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
