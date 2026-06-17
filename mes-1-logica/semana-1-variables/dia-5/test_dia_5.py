#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    21: [
        ("5 1\n", ["MULT=10", "DIV=2"], "N=5, K=1 -> MULT=10, DIV=2"),
        ("32 3\n", ["MULT=256", "DIV=4"], "N=32, K=3 -> MULT=256, DIV=4"),
        ("-8 2\n", ["MULT=-32", "DIV=-2"], "N=-8, K=2 -> MULT=-32, DIV=-2"),
        ("1000 0\n", ["MULT=1000", "DIV=1000"], "N=1000, K=0 -> MULT=1000, DIV=1000"),
    ],
    22: [
        ("5 2\n", ["BIT=1"], "N=5 (0101), P=2 -> 1"),
        ("5 1\n", ["BIT=0"], "N=5 (0101), P=1 -> 0"),
        ("1024 10\n", ["BIT=1"], "N=1024 (2^10), P=10 -> 1"),
        ("1024 9\n", ["BIT=0"], "N=1024 (2^10), P=9 -> 0"),
        ("-1 31\n", ["BIT=1"], "N=-1 (todos 1), P=31 -> 1"),
    ],
    23: [
        ("2 4\n", ["MASCARA=28"], "L=2, R=4 -> 28 (bits 2, 3, 4)"),
        ("0 0\n", ["MASCARA=1"], "L=0, R=0 -> 1 (bit 0)"),
        ("0 31\n", ["MASCARA=4294967295"], "L=0, R=31 -> 4294967295 (todos los bits)"),
        ("8 15\n", ["MASCARA=65280"], "L=8, R=15 -> 65280 (0xFF00)"),
    ],
    24: [
        ("0\n", ["CANTIDAD=0"], "B=0 -> 0 bits"),
        ("255\n", ["CANTIDAD=8"], "B=255 -> 8 bits"),
        ("100\n", ["CANTIDAD=3"], "B=100 (01100100) -> 3 bits"),
        ("129\n", ["CANTIDAD=2"], "B=129 (10000001) -> 2 bits"),
    ],
    25: [
        ("100\n", ["NUEVO=70"], "B=100 (0110 0100) -> 70 (0100 0110)"),
        ("255\n", ["NUEVO=255"], "B=255 (1111 1111) -> 255 (1111 1111)"),
        ("0\n", ["NUEVO=0"], "B=0 (0000 0000) -> 0"),
        ("9\n", ["NUEVO=144"], "B=9 (0000 1001) -> 144 (1001 0000)"),
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
        print(f"❌ Reto {reto_num} inválido para el Día 5.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
