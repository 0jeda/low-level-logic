#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

TEST_CASES = {
    66: [
        ("7\n4 5 6 7 0 1 2\n0\n", ["INDICE=4"], "Rotado: buscar el 0"),
        ("7\n4 5 6 7 0 1 2\n3\n", ["INDICE=-1"], "Rotado: buscar ausente (3)"),
        ("5\n3 4 5 1 2\n4\n", ["INDICE=1"], "Rotado pequeño: buscar el 4"),
    ],
    67: [
        ("4\n1 2 8 9\n4\n", ["CERCANO=2"], "Más cercano sin empate (2 está a dist 2, 8 está a dist 4)"),
        ("4\n1 2 8 9\n5\n", ["CERCANO=2"], "Empate de distancia (2 y 8 están a dist 3, elegir el menor: 2)"),
        ("5\n1 5 10 15 20\n16\n", ["CERCANO=15"], "Más cercano (15 a dist 1, 20 a dist 4)"),
        ("1\n42\n100\n", ["CERCANO=42"], "Un solo elemento"),
    ],
    68: [
        ("4\n1 2 2 4\n4\n2 2 3 5\n", ["INTERSECCION=2"], "Intersección con repetidos (salida única 2)"),
        ("5\n1 2 3 4 5\n5\n2 4 6 8 10\n", ["INTERSECCION=2 4"], "Intersección múltiple ordenada"),
        ("3\n1 3 5\n3\n2 4 6\n", ["INTERSECCION="], "Intersección vacía"),
    ],
    69: [
        ("5\n1 4 2 8 5\n8\n", ["PAREJA3=SI"], "Pareja de 3 encontrada (1 + 2 + 5 = 8)"),
        ("5\n1 4 2 8 5\n20\n", ["PAREJA3=NO"], "Pareja de 3 no encontrada (suma excede el máximo)"),
        ("3\n1 2 3\n6\n", ["PAREJA3=SI"], "Exactamente los 3 elementos suman 6"),
        ("4\n1 2 3 4\n5\n", ["PAREJA3=NO"], "Suma muy pequeña (mínima suma posible es 6)"),
    ],
    70: [
        ("1\n", ["COMPARACIONES=1"], "N=1 -> 1 comparación"),
        ("2\n", ["COMPARACIONES=2"], "N=2 -> 2 comparaciones"),
        ("3\n", ["COMPARACIONES=2"], "N=3 -> 2 comparaciones"),
        ("4\n", ["COMPARACIONES=3"], "N=4 -> 3 comparaciones"),
        ("1000\n", ["COMPARACIONES=10"], "N=1000 -> 10 comparaciones"),
        ("2000000000\n", ["COMPARACIONES=31"], "N=2,000,000,000 -> 31 comparaciones"),
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
        print(f"❌ Reto {reto_num} inválido para el Día 7 de la Semana 2.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
