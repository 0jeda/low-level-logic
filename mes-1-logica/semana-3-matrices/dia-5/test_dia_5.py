#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    91: [
        ("3 3\n10 20 30\n15 25 35\n27 29 37\n29\n", ["POSICION=(2,1)"], "Objetivo 29 en (2,1)"),
        ("3 3\n10 20 30\n15 25 35\n27 29 37\n99\n", ["ERROR"], "Objetivo ausente"),
        ("2 2\n1 2\n3 4\n1\n", ["POSICION=(0,0)"], "Objetivo en la celda (0,0)"),
    ],
    92: [
        ("3 4\n0 0 1 1\n0 1 1 1\n0 0 0 1\n", ["FILA=2"], "Fila 2 tiene tres ceros (máximo)"),
        ("3 3\n1 1 1\n1 1 1\n1 1 1\n", ["FILA=0"], "Cero ceros, devuelve fila 0"),
        ("2 2\n0 0\n0 0\n", ["FILA=0"], "Empate, devuelve menor índice de fila (0)"),
    ],
    93: [
        ("3 3\n1 2 3\n4 5 6\n7 8 9\n2\n0 0 2 2\n1 1 2 2\n", ["SUMA=45", "SUMA=28"], "Dos consultas en matriz 3x3"),
        ("2 2\n1 2\n3 4\n1\n0 1 1 1\n", ["SUMA=6"], "Suma de columna 1"),
    ],
    94: [
        ("2 3\n1 2 3\n4 5 6\n1 2 3\n", ["VECTOR=14 32"], "Producto matriz 2x3 por vector 3"),
        ("3 2\n1 0\n0 1\n5 -5\n2 3\n", ["VECTOR=2 3 -5"], "Producto matriz 3x2 por vector 2"),
    ],
    95: [
        ("3 3\n1 2 3\n4 5 6\n7 8 9\n", ["SILLA=7 EN (2,0)"], "Punto de silla 7 en (2,0)"),
        ("2 2\n1 2\n3 4\n", ["SILLA=3 EN (1,0)"], "Punto de silla 3 en (1,0)"),
        ("3 3\n1 2 3\n3 2 1\n1 2 3\n", ["NINGUNO"], "Matriz sin puntos de silla"),
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
        for idx, (entrada, esperados, desc) in enumerate(casos, 1):
            try:
                salida = ejecutar_caso(ruta_bin, entrada)
                if validar(salida, esperados):
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
        print("Uso: python3 test_dia_5.py <ruta_cpp> | all")
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
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_5.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 5 de la Semana 3.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
