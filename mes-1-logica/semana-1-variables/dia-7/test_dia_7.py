#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    31: [
        ("5\n", ["BITS=2"], "N=5 (101) -> 2 bits"),
        ("0\n", ["BITS=0"], "N=0 -> 0 bits"),
        ("-1\n", ["BITS=32"], "N=-1 (todos 1) -> 32 bits"),
        ("2147483647\n", ["BITS=31"], "N=INT_MAX -> 31 bits"),
        ("-2147483648\n", ["BITS=1"], "N=INT_MIN (solo MSB) -> 1 bit"),
    ],
    32: [
        ("1\n", ["POTENCIA=SI"], "N=1 -> Si (2^0)"),
        ("2\n", ["POTENCIA=SI"], "N=2 -> Si (2^1)"),
        ("1024\n", ["POTENCIA=SI"], "N=1024 -> Si (2^10)"),
        ("0\n", ["POTENCIA=NO"], "N=0 -> No"),
        ("-8\n", ["POTENCIA=NO"], "N=-8 -> No"),
        ("5\n", ["POTENCIA=NO"], "N=5 -> No"),
        ("2147483647\n", ["POTENCIA=NO"], "N=INT_MAX -> No"),
    ],
    33: [
        ("156\n", ["RACHA=3"], "N=156 (10011100) -> racha de 3"),
        ("0\n", ["RACHA=0"], "N=0 -> racha de 0"),
        ("-1\n", ["RACHA=32"], "N=-1 (todos 1) -> racha de 32"),
        ("5\n", ["RACHA=1"], "N=5 (101) -> racha de 1"),
        ("15\n", ["RACHA=4"], "N=15 (1111) -> racha de 4"),
    ],
    34: [
        ("0\n", ["REVERSADO=0"], "N=0 -> 0"),
        ("4294967295\n", ["REVERSADO=4294967295"], "N=Max -> Max"),
        ("1\n", ["REVERSADO=2147483648"], "N=1 (bit 0) -> 2147483648 (bit 31)"),
        ("2\n", ["REVERSADO=1073741824"], "N=2 (bit 1) -> 1073741824 (bit 30)"),
        ("3\n", ["REVERSADO=3221225472"], "N=3 (bits 0,1) -> 3221225472 (bits 31,30)"),
    ],
    35: [
        ("1 0 0 0 0\n", ["RES=0", "COUT=0"], "1 AND 0 -> RES=0, COUT=0"),
        ("1 1 0 0 0\n", ["RES=1", "COUT=0"], "1 AND 1 -> RES=1, COUT=0"),
        ("1 0 0 0 1\n", ["RES=1", "COUT=0"], "1 OR 0 -> RES=1, COUT=0"),
        ("0 0 0 0 1\n", ["RES=0", "COUT=0"], "0 OR 0 -> RES=0, COUT=0"),
        ("1 1 0 1 0\n", ["RES=0", "COUT=0"], "1 XOR 1 -> RES=0, COUT=0"),
        ("1 0 0 1 0\n", ["RES=1", "COUT=0"], "1 XOR 0 -> RES=1, COUT=0"),
        ("1 1 0 1 1\n", ["RES=0", "COUT=1"], "SUM: 1 + 1 + cin=0 -> RES=0, COUT=1"),
        ("1 1 1 1 1\n", ["RES=1", "COUT=1"], "SUM: 1 + 1 + cin=1 -> RES=1, COUT=1"),
        ("0 1 1 1 1\n", ["RES=0", "COUT=1"], "SUM: 0 + 1 + cin=1 -> RES=0, COUT=1"),
        ("0 1 0 1 1\n", ["RES=1", "COUT=0"], "SUM: 0 + 1 + cin=0 -> RES=1, COUT=0"),
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
        print("Uso: python3 test_dia_7.py <ruta_cpp> | all")
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
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_7.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 7.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
