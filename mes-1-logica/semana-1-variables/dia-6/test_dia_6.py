#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    26: [
        ("ABCD", ["ENTERO=1094861636"], "C1='A', C2='B', C3='C', C4='D' -> 1094861636"),
        ("test", ["ENTERO=1952805748"], "C1='t', C2='e', C3='s', C4='t' -> 1952805748"),
        ("    ", ["ENTERO=538976288"], "Cuatro espacios -> 538976288"),
    ],
    27: [
        ("1094861636\n", ["CHARS=A B C D"], "1094861636 -> A B C D"),
        ("1952805748\n", ["CHARS=t e s t"], "1952805748 -> t e s t"),
        ("538976288\n", ["CHARS=      "], "538976288 -> Cuatro espacios"),
    ],
    28: [
        ("10 2\n", ["ROTADO=40"], "N=10, R=2 -> 40"),
        ("2147483648 1\n", ["ROTADO=1"], "N=2^31, R=1 -> 1 (bit de signo pasa al bit 0)"),
        ("4294967295 10\n", ["ROTADO=4294967295"], "N=Max, R=10 -> Max"),
        ("12345678 0\n", ["ROTADO=12345678"], "N=12345678, R=0 -> 12345678 (caso borde seguro)"),
    ],
    29: [
        ("129\n", ["PALINDROMO=ES_PALINDROMO"], "B=129 (10000001) -> Si"),
        ("100\n", ["PALINDROMO=NO_ES_PALINDROMO"], "B=100 (01100100) -> No"),
        ("0\n", ["PALINDROMO=ES_PALINDROMO"], "B=0 (00000000) -> Si"),
        ("255\n", ["PALINDROMO=ES_PALINDROMO"], "B=255 (11111111) -> Si"),
        ("165\n", ["PALINDROMO=ES_PALINDROMO"], "B=165 (10100101) -> Si"),
        ("90\n", ["PALINDROMO=ES_PALINDROMO"], "B=90 (01011010) -> Si"),
        ("1\n", ["PALINDROMO=NO_ES_PALINDROMO"], "B=1 (00000001) -> No"),
    ],
    30: [
        ("5\n", ["RESULTADO=6"], "N=5 -> 6"),
        ("0\n", ["RESULTADO=1"], "N=0 -> 1"),
        ("-1\n", ["RESULTADO=0"], "N=-1 -> 0"),
        ("-100\n", ["RESULTADO=-99"], "N=-100 -> -99"),
        ("2147483647\n", ["RESULTADO=-2147483648"], "N=INT_MAX -> INT_MIN (desbordamiento de acarreo)"),
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
        print(f"❌ Reto {reto_num} inválido para el Día 6.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
