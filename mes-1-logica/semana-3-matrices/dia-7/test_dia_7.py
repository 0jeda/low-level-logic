#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

VALID_SUDOKU = (
    "5 3 4 6 7 8 9 1 2\n"
    "6 7 2 1 9 5 3 4 8\n"
    "1 9 8 3 4 2 5 6 7\n"
    "8 5 9 7 6 1 4 2 3\n"
    "4 2 6 8 5 3 7 9 1\n"
    "7 1 3 9 2 4 8 5 6\n"
    "9 6 1 5 3 7 2 8 4\n"
    "2 8 7 4 1 9 6 3 5\n"
    "3 4 5 2 8 6 1 7 9\n"
)

INVALID_SUDOKU = (
    "3 3 4 6 7 8 9 1 2\n"  # Duplicado el 3 en fila 0
    "6 7 2 1 9 5 3 4 8\n"
    "1 9 8 3 4 2 5 6 7\n"
    "8 5 9 7 6 1 4 2 3\n"
    "4 2 6 8 5 3 7 9 1\n"
    "7 1 3 9 2 4 8 5 6\n"
    "9 6 1 5 3 7 2 8 4\n"
    "2 8 7 4 1 9 6 3 5\n"
    "3 4 5 2 8 6 1 7 9\n"
)

TEST_CASES = {
    101: [
        ("3 3\n0 -1 0\n0 0 0\n-1 0 -1\n", ["TABLERO=", "1 -1 1", "2 3 2", "-1 2 -1"], "Matriz 3x3 Buscaminas básica"),
        ("1 1\n-1\n", ["TABLERO=", "-1"], "Matriz 1x1 con una sola mina"),
    ],
    102: [
        ("3\n1 2 3\n4 5 6\n7 8 9\n", ["ROTADA=", "3 6 9", "2 5 8", "1 4 7"], "Rotación antihorario 3x3"),
        ("2\n1 2\n3 4\n", ["ROTADA=", "2 4", "1 3"], "Rotación antihorario 2x2"),
    ],
    103: [
        ("3 3\n", ["SERPIENTE=", "1 2 3", "6 5 4", "7 8 9"], "Matriz serpiente 3x3"),
        ("2 4\n", ["SERPIENTE=", "1 2 3 4", "8 7 6 5"], "Matriz serpiente 2x4"),
    ],
    104: [
        ("3\n", ["CARACOL=", "1 2 3", "8 9 4", "7 6 5"], "Matriz caracol 3x3"),
        ("2\n", ["CARACOL=", "1 2", "4 3"], "Matriz caracol 2x2"),
    ],
    105: [
        (VALID_SUDOKU, ["SUDOKU=VALIDO"], "Sudoku completamente lleno y válido"),
        (INVALID_SUDOKU, ["SUDOKU=INVALIDO"], "Sudoku inválido por duplicado de número 3 en fila 0"),
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
        print(f"❌ Reto {reto_num} inválido para el Día 7 de la Semana 3.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
