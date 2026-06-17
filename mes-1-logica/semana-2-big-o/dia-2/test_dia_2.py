#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    41: [
        ("5\n1 2 3 4 5\n", ["DUPLICADOS=NO"], "Arreglo sin duplicados"),
        ("5\n1 3 2 3 5\n", ["DUPLICADOS=SI"], "Arreglo con duplicados (el 3)"),
        ("2\n42 42\n", ["DUPLICADOS=SI"], "Dos elementos iguales"),
    ],
    42: [
        ("5\n1 10 2 20 5\n", ["DIFERENCIA=19"], "Valores positivos (20 - 1 = 19)"),
        ("3\n-5 0 5\n", ["DIFERENCIA=10"], "Valores mixtos (5 - (-5) = 10)"),
        ("2\n42 42\n", ["DIFERENCIA=0"], "Valores idénticos"),
    ],
    43: [
        ("5\n4 2 1 2 5\n3\n2 3 5\n", ["INTERSECCION=2 5"], "Intersección con repetidos y orden de Arr1"),
        ("3\n1 2 3\n3\n4 5 6\n", ["INTERSECCION="], "Sin intersección"),
        ("4\n10 20 30 10\n4\n30 40 10 50\n", ["INTERSECCION=10 30"], "Intersección en orden Arr1 sin duplicados en salida"),
    ],
    44: [
        ("5\n1 2 3 4 5\n2\n", ["ROTADO=4 5 1 2 3"], "Rotación normal (K=2)"),
        ("3\n10 20 30\n0\n", ["ROTADO=10 20 30"], "Rotación cero (K=0)"),
        ("4\n1 2 3 4\n6\n", ["ROTADO=3 4 1 2"], "Rotación mayor a N (K=6 -> 6%4=2)"),
    ],
    45: [
        ("5\n1 4 2 8 5\n7\n", ["PAREJA=SI"], "Pareja encontrada (2 + 5 = 7)"),
        ("5\n1 4 2 8 5\n11\n", ["PAREJA=NO"], "Pareja no encontrada (no hay suma 11)"),
        ("3\n3 1 4\n6\n", ["PAREJA=NO"], "Pareja no encontrada (no se puede usar el mismo elemento 3 dos veces)"),
        ("4\n3 3 1 4\n6\n", ["PAREJA=SI"], "Pareja encontrada (dos elementos 3 independientes)"),
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
        print("Uso: python3 test_dia_2.py <ruta_cpp> | all")
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
            print("❌ No se pudo determinar el número de reto. Especifica: test_dia_2.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 2 de la Semana 2.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
