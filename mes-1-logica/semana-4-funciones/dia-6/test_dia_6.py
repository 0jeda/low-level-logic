#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

# Para el reto 134, la salida esperada es dinámica (debe coincidir con DECAYED_SIZE=4 o DECAYED_SIZE=8)
TEST_CASES = {
    131: [
        ("42\n", ["VALOR=52"], "Sumar 10 a 42"),
        ("-10\n", ["VALOR=0"], "Sumar 10 a -10"),
    ],
    132: [
        ("5\n1 2 3 4 5\n", ["SUMA=15"], "Suma de 1 a 5 con ptr++"),
        ("3\n10 -2 5\n", ["SUMA=13"], "Suma con negativos con ptr++"),
    ],
    133: [
        ("100 200\n", ["A=200", "B=100"], "Swap de 100 y 200 con punteros"),
        ("-5 8\n", ["A=8", "B=-5"], "Swap de -5 y 8 con punteros"),
    ],
    134: [
        ("\n", ["LOCAL_SIZE=40", "DECAYED_SIZE=MATCH_PTR"], "Validar decay de tamaño del arreglo"),
    ],
    135: [
        ("5\n10 20 50 30 40\n", ["INDICE=2", "VALOR=50"], "Máximo al medio"),
        ("4\n-10 -5 -20 -15\n", ["INDICE=1", "VALOR=-5"], "Máximo con negativos"),
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
        if esperada == "DECAYED_SIZE=MATCH_PTR":
            # Debe ser DECAYED_SIZE=4 o DECAYED_SIZE=8
            if obtenida in ["DECAYED_SIZE=4", "DECAYED_SIZE=8"]:
                continue
            else:
                print(f"      [ERROR] Línea {idx + 1} incorrecta.")
                print(f"              Esperada: DECAYED_SIZE=4 o DECAYED_SIZE=8")
                print(f"              Obtenida: {obtenida}")
                return False
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
        print("Uso: python3 test_dia_6.py <ruta_cpp> | all")
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
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_6.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 6 de la Semana 4.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
