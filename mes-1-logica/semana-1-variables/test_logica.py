#!/usr/bin/env python3
"""
test_logica.py – Pruebas automáticas para el Reto 1: El Intercambio de Variables.

Uso:
    python3 test_logica.py                         # prueba plantilla.cpp (sin solución → falla esperada)
    python3 test_logica.py soluciones/tu_nombre.cpp

El script:
  1. Compila el archivo .cpp indicado con  g++ -O2.
  2. Ejecuta el binario con varios casos de prueba.
  3. Valida la salida con assert; imprime un resumen al final.
"""

import subprocess
import sys
import os
import tempfile

# ---------------------------------------------------------------------------
# Casos de prueba: (A, B, A_esperado, B_esperado, descripción)
# ---------------------------------------------------------------------------
CASOS = [
    (5,    10,   10,    5,    "A=5,  B=10  →  A=10, B=5"),
    (-3,   7,    7,    -3,    "A=-3, B=7   →  A=7,  B=-3"),
    (0,    0,    0,     0,    "A=0,  B=0   →  A=0,  B=0"),
    (100, -100, -100,  100,   "A=100, B=-100  →  A=-100, B=100"),
    (-42, -1,   -1,   -42,   "A=-42, B=-1  →  A=-1, B=-42"),
]


def compilar(ruta_cpp: str) -> str:
    """Compila el archivo indicado y devuelve la ruta del binario temporal."""
    fd, ruta_bin = tempfile.mkstemp(prefix="reto1_", suffix="")
    os.close(fd)

    resultado = subprocess.run(
        ["g++", "-O2", "-o", ruta_bin, ruta_cpp],
        capture_output=True,
        text=True,
    )

    if resultado.returncode != 0:
        print("❌ Error de compilación:")
        print(resultado.stderr)
        os.unlink(ruta_bin)
        sys.exit(1)

    return ruta_bin


def ejecutar(ruta_bin: str, a: int, b: int) -> str:
    """Ejecuta el binario con la entrada dada y devuelve stdout."""
    resultado = subprocess.run(
        [ruta_bin],
        input=f"{a} {b}\n",
        capture_output=True,
        text=True,
        timeout=5,
    )
    return resultado.stdout.strip()


def validar_salida(salida: str, a_esp: int, b_esp: int) -> None:
    """Lanza AssertionError si la salida no coincide con los valores esperados."""
    lineas = salida.splitlines()
    assert len(lineas) == 2, (
        f"Se esperaban 2 líneas de salida, se obtuvieron {len(lineas)}.\n"
        f"Salida recibida:\n{salida}"
    )

    assert lineas[0] == f"A={a_esp}", (
        f"Línea 1 incorrecta.\n"
        f"  Esperado : A={a_esp}\n"
        f"  Obtenido : {lineas[0]}"
    )

    assert lineas[1] == f"B={b_esp}", (
        f"Línea 2 incorrecta.\n"
        f"  Esperado : B={b_esp}\n"
        f"  Obtenido : {lineas[1]}"
    )


def main() -> None:
    # Determinar el archivo a probar
    if len(sys.argv) > 1:
        ruta_cpp = sys.argv[1]
    else:
        ruta_cpp = os.path.join(os.path.dirname(__file__), "plantilla.cpp")
        print(f"ℹ️  No se indicó archivo. Probando: {ruta_cpp}\n")

    if not os.path.isfile(ruta_cpp):
        print(f"❌ Archivo no encontrado: {ruta_cpp}")
        sys.exit(1)

    print(f"🔨 Compilando: {ruta_cpp}")
    ruta_bin = compilar(ruta_cpp)

    print("🧪 Ejecutando casos de prueba...\n")
    fallos = 0

    try:
        for idx, (a, b, a_esp, b_esp, desc) in enumerate(CASOS, start=1):
            salida = ejecutar(ruta_bin, a, b)
            try:
                validar_salida(salida, a_esp, b_esp)
                print(f"  [OK] Caso {idx}: {desc}")
            except AssertionError as err:
                print(f"  [FALLO] Caso {idx}: {desc}")
                print(f"          {err}")
                fallos += 1
    finally:
        os.unlink(ruta_bin)

    print()
    if fallos == 0:
        print("✅ ¡Todos los casos de prueba pasaron!")
        sys.exit(0)
    else:
        print(f"❌ {fallos} caso(s) fallaron. Revisa tu lógica e intenta de nuevo.")
        sys.exit(1)


if __name__ == "__main__":
    main()
