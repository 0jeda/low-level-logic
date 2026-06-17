#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

# ---------------------------------------------------------------------------
# Definición de Casos de Prueba por Reto
# ---------------------------------------------------------------------------
TEST_CASES = {
    1: [
        # (entrada, salida_esperada_lineas, descripcion)
        ("5 10\n", ["A=10", "B=5"], "A=5, B=10 -> A=10, B=5"),
        ("-3 7\n", ["A=7", "B=-3"], "A=-3, B=7 -> A=7, B=-3"),
        ("0 0\n", ["A=0", "B=0"], "A=0, B=0 -> A=0, B=0"),
        ("100 -100\n", ["A=-100", "B=100"], "A=100, B=-100 -> A=-100, B=100"),
    ],
    2: [
        ("10 20\n", ["30"], "Suma común (10 + 20 = 30)"),
        ("2147483640 10\n", ["OVERFLOW"], "Desbordamiento superior (2147483640 + 10)"),
        ("-2147483640 -10\n", ["UNDERFLOW"], "Desbordamiento inferior (-2147483640 + -10)"),
        ("-100 50\n", ["-50"], "Suma con signos opuestos (-100 + 50 = -50)"),
        ("2147483647 0\n", ["2147483647"], "Límite superior con cero"),
        ("-2147483648 0\n", ["-2147483648"], "Límite inferior con cero"),
    ],
    3: [
        ("100000\n", ["INT=100000", "SHORT=-31072"], "Cast de 100,000 (cabe en int, desborda short)"),
        ("4294967295\n", ["INT=-1", "SHORT=-1"], "Cast de 4,294,967,295 (oxFFFFFFFF)"),
        ("5\n", ["INT=5", "SHORT=5"], "Cast de 5 (cabe en ambos)"),
        ("9223372036854775807\n", ["INT=-1", "SHORT=-1"], "Cast del máximo long long"),
    ],
    4: [
        ("2000000000 2\n", ["PRODUCTO=4000000000"], "Multiplicación que desborda 32 bits (2e9 * 2)"),
        ("-2000000000 2\n", ["PRODUCTO=-4000000000"], "Multiplicación negativa que desborda 32-bits"),
        ("1000000 1000000\n", ["PRODUCTO=1000000000000"], "Multiplicación de un millón por un millón"),
    ],
    5: [
        ("5 10\n", ["RESULTADO=4294967291"], "Resta con underflow (5 - 10)"),
        ("10 5\n", ["RESULTADO=5"], "Resta común sin underflow (10 - 5)"),
        ("0 1\n", ["RESULTADO=4294967295"], "Resta con underflow mínimo (0 - 1)"),
    ]
}

def compilar(ruta_cpp: str) -> str:
    """Compila el archivo .cpp a un binario temporal y devuelve su ruta."""
    fd, ruta_bin = tempfile.mkstemp(prefix="test_reto_", suffix="")
    os.close(fd)

    res = subprocess.run(
        ["g++", "-O2", "-o", ruta_bin, ruta_cpp],
        capture_output=True,
        text=True
    )
    if res.returncode != 0:
        print("❌ Error de compilación:")
        print(res.stderr)
        try:
            os.unlink(ruta_bin)
        except OSError:
            pass
        sys.exit(1)
    return ruta_bin

def ejecutar_caso(ruta_bin: str, entrada: str) -> str:
    """Ejecuta el binario con la entrada dada y devuelve la salida estándar limpia."""
    res = subprocess.run(
        [ruta_bin],
        input=entrada,
        capture_output=True,
        text=True,
        timeout=3
    )
    return res.stdout.strip()

def validar(salida: str, esperados: list) -> bool:
    """Valida si cada una de las líneas esperadas se encuentra en la salida."""
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
                print(f"  [TIMEOUT] Caso {idx}: {desc} (El programa tardó más de 3 segundos)")
            except Exception as e:
                print(f"  [ERROR] Caso {idx}: {desc} ({e})")
    finally:
        try:
            os.unlink(ruta_bin)
        except OSError:
            pass

    total = len(casos)
    if exitos == total:
        print(f"✅ Reto {reto_num}: ¡Pasaron todos los casos ({exitos}/{total})!\n")
        return True
    else:
        print(f"❌ Reto {reto_num}: Fallaron {total - exitos} de {total} casos.\n")
        return False

def detectar_reto(ruta: str) -> int:
    """Extrae el número de reto del nombre de archivo (ej: reto_2.cpp -> 2)."""
    match = re.search(r'reto_?(\d)', os.path.basename(ruta))
    if match:
        return int(match.group(1))
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 test_dia_1.py <ruta_cpp>")
        print("  python3 test_dia_1.py <numero_reto> <ruta_cpp>")
        print("  python3 test_dia_1.py all")
        sys.exit(1)

    # Caso 1: python3 test_dia_1.py all
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
            if not encontrado:
                # Comprobar si hay plantilla para correr y avisar
                pass

        if retos_probados == 0:
            print("ℹ️ No se encontraron soluciones en la carpeta 'soluciones/' para probar.")
            print("Copia una plantilla a 'soluciones/reto_X.cpp' y resuélvela.")
            sys.exit(0)

        if exito_total:
            print("🎉 ¡Excelente! Todas las soluciones que creaste para hoy pasaron las pruebas.")
            sys.exit(0)
        else:
            print("❌ Algunas soluciones fallaron. Revisa el registro arriba.")
            sys.exit(1)

    # Caso 2: python3 test_dia_1.py <numero_reto> <ruta_cpp>
    if len(sys.argv) == 3:
        try:
            reto_num = int(sys.argv[1])
            ruta_cpp = sys.argv[2]
        except ValueError:
            print("❌ El número de reto debe ser un entero.")
            sys.exit(1)
    # Caso 3: python3 test_dia_1.py <ruta_cpp> (intenta detectar número de reto)
    else:
        ruta_cpp = sys.argv[1]
        reto_num = detectar_reto(ruta_cpp)
        if not reto_num:
            print("❌ No se pudo determinar el número de reto a partir del nombre del archivo.")
            print("Por favor especifícalo: python3 test_dia_1.py <numero_reto> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto número {reto_num} inválido. Debe estar entre 1 y 5.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
