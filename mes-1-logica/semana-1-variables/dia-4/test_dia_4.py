#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    16: [
        ("4\n", ["PAR"], "4 es Par"),
        ("7\n", ["IMPAR"], "7 es Impar"),
        ("0\n", ["PAR"], "0 es Par"),
        ("-1\n", ["IMPAR"], "-1 es Impar"),
        ("-2\n", ["PAR"], "-2 es Par"),
    ],
    17: [
        ("5 10\n", ["A=10", "B=5"], "A=5, B=10 -> A=10, B=5"),
        ("-3 7\n", ["A=7", "B=-3"], "A=-3, B=7 -> A=7, B=-3"),
        ("0 0\n", ["A=0", "B=0"], "A=0, B=0 -> A=0, B=0"),
        ("100 -100\n", ["A=-100", "B=100"], "A=100, B=-100 -> A=-100, B=100"),
    ],
    18: [
        ("7 1\n", ["RESULTADO=5"], "N=7 (0111), P=1 -> 5 (0101)"),
        ("15 0\n", ["RESULTADO=14"], "N=15 (1111), P=0 -> 14 (1110)"),
        ("0 5\n", ["RESULTADO=0"], "N=0, P=5 -> 0"),
        ("-1 31\n", ["RESULTADO=2147483647"], "N=-1 (todos 1), P=31 -> 2147483647 (sin bit de signo)"),
    ],
    19: [
        ("4 1\n", ["RESULTADO=6"], "N=4 (0100), P=1 -> 6 (0110)"),
        ("0 0\n", ["RESULTADO=1"], "N=0, P=0 -> 1 (0001)"),
        ("5 2\n", ["RESULTADO=5"], "N=5 (0101), P=2 -> 5 (ya encendido)"),
        ("2147483647 31\n", ["RESULTADO=-1"], "N=INT_MAX, P=31 -> -1 (todos 1)"),
    ],
    20: [
        ("5\n", ["NOT=-6", "NEG=-5"], "N=5 -> NOT=-6, NEG=-5"),
        ("-1\n", ["NOT=0", "NEG=1"], "N=-1 -> NOT=0, NEG=1"),
        ("0\n", ["NOT=-1", "NEG=0"], "N=0 -> NOT=-1, NEG=0"),
        ("2147483647\n", ["NOT=-2147483648", "NEG=-2147483647"], "N=INT_MAX -> NOT=INT_MIN, NEG=-INT_MAX"),
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
    if match:
        return int(match.group(1))
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 test_dia_4.py <ruta_cpp> | all")
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
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_4.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 4.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
