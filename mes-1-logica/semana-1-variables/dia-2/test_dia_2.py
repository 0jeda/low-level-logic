#!/usr/bin/env python3
import subprocess
import sys
import os
import tempfile
import re

# Helper to check float similarity
def float_cercano(val1, val2, epsilon=1e-5):
    try:
        return abs(float(val1) - float(val2)) <= epsilon
    except ValueError:
        return False

def validar_reto6(salida):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 1:
        return False, f"Se esperaba 1 línea de salida, se recibieron {len(lineas)}."
    if lineas[0] not in ["IGUALES", "DIFERENTES"]:
        return False, f"La salida debe ser 'IGUALES' o 'DIFERENTES'. Obtenido: {lineas[0]}"
    return True, lineas[0]

def validar_reto7(salida, trunc_esp, red_esp, piso_esp):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 3:
        return False, f"Se esperaban 3 líneas de salida (TRUNC, REDONDEO, PISO), se recibieron {len(lineas)}."
    
    dict_salida = {}
    for l in lineas:
        if '=' not in l:
            return False, f"Formato incorrecto. Se esperaba CLAVE=valor, obtenido: {l}"
        k, v = l.split('=', 1)
        dict_salida[k.upper()] = v.strip()

    for k, esp in [("TRUNC", trunc_esp), ("REDONDEO", red_esp), ("PISO", piso_esp)]:
        if k not in dict_salida:
            return False, f"Falta la clave {k} en la salida."
        try:
            val_obtenido = int(dict_salida[k])
            if val_obtenido != esp:
                return False, f"Para {k}, esperado: {esp}, obtenido: {val_obtenido}"
        except ValueError:
            return False, f"El valor para {k} debe ser entero. Obtenido: {dict_salida[k]}"
            
    return True, ""

def validar_reto8(salida, c_esperado):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 1:
        return False, f"Se esperaba 1 línea de salida (C=...), se recibieron {len(lineas)}."
    if '=' not in lineas[0]:
        return False, f"Formato incorrecto. Se esperaba C=valor, obtenido: {lineas[0]}"
    k, v = lineas[0].split('=', 1)
    if k.upper() != 'C':
        return False, f"Clave incorrecta. Esperada: C, obtenida: {k}"
    if not float_cercano(v, c_esperado, epsilon=1e-3):
        return False, f"Esperado: C={c_esperado}, obtenido: C={v}"
    return True, ""

def validar_reto9(salida, tipo_esperado, valor_esperado=None):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 1:
        return False, f"Se esperaba 1 línea de salida (RESULTADO=...), se recibieron {len(lineas)}."
    if '=' not in lineas[0]:
        return False, f"Formato incorrecto. Se esperaba RESULTADO=valor, obtenido: {lineas[0]}"
    k, v = lineas[0].split('=', 1)
    if k.upper() != 'RESULTADO':
        return False, f"Clave incorrecta. Esperada: RESULTADO, obtenida: {k}"
    
    val_obtenido = v.strip().upper()
    if tipo_esperado in ["INF", "-INF", "NAN"]:
        if val_obtenido != tipo_esperado:
            return False, f"Esperado: RESULTADO={tipo_esperado}, obtenido: RESULTADO={val_obtenido}"
    else:
        # Es un número
        if not float_cercano(val_obtenido, valor_esperado, epsilon=1e-3):
            return False, f"Esperado: RESULTADO={valor_esperado}, obtenido: RESULTADO={val_obtenido}"
    return True, ""

def validar_reto10(salida, f_esp, d_esp):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    if len(lineas) != 2:
        return False, f"Se esperaban 2 líneas de salida (FLOAT, DOUBLE), se recibieron {len(lineas)}."
    
    dict_salida = {}
    for l in lineas:
        if '=' not in l:
            return False, f"Formato incorrecto. Se esperaba CLAVE=valor, obtenido: {l}"
        k, v = l.split('=', 1)
        dict_salida[k.upper()] = v.strip()

    for k, esp in [("FLOAT", f_esp), ("DOUBLE", d_esp)]:
        if k not in dict_salida:
            return False, f"Falta la clave {k} en la salida."
        if not float_cercano(dict_salida[k], esp, epsilon=5.0): # Toleramos un margen debido a posibles representaciones
            return False, f"Para {k}, esperado cercano a: {esp}, obtenido: {dict_salida[k]}"
            
    return True, ""

# ---------------------------------------------------------------------------
# Casos de prueba por Reto
# ---------------------------------------------------------------------------
TEST_CASES = {
    6: [
        ("0.1 0.2 0.3\n", "IGUALES", "0.1 + 0.2 ≈ 0.3"),
        ("0.1000001 0.2 0.3\n", "IGUALES", "0.1000001 + 0.2 ≈ 0.3"),
        ("0.1 0.2 0.30001\n", "DIFERENTES", "0.1 + 0.2 != 0.30001"),
        ("100.0 -50.0 50.0\n", "IGUALES", "100.0 + -50.0 ≈ 50.0"),
    ],
    7: [
        ("3.7\n", (3, 4, 3), "Positivo con decimal alto (3.7)"),
        ("-3.7\n", (-3, -4, -4), "Negativo con decimal alto (-3.7)"),
        ("5.0\n", (5, 5, 5), "Entero exacto positivo (5.0)"),
        ("-5.0\n", (-5, -5, -5), "Entero exacto negativo (-5.0)"),
        ("-0.2\n", (0, 0, -1), "Fracción negativa menor a 0.5 (-0.2)"),
        ("-0.5\n", (0, -1, -1), "Límite del redondeo negativo (-0.5)"),
        ("0.5\n", (0, 1, 0), "Límite del redondeo positivo (0.5)"),
    ],
    8: [
        ("32\n", 0.0, "Punto de congelación (32 F -> 0 C)"),
        ("212\n", 100.0, "Punto de ebullición (212 F -> 100 C)"),
        ("-40\n", -40.0, "Escala cruzada (-40 F -> -40 C)"),
        ("98.6\n", 37.0, "Temperatura corporal normal (98.6 F -> 37 C)"),
    ],
    9: [
        ("5.0 0.0\n", ("INF", None), "División 5.0 / 0.0 -> INF"),
        ("-5.0 0.0\n", ("-INF", None), "División -5.0 / 0.0 -> -INF"),
        ("0.0 0.0\n", ("NAN", None), "División 0.0 / 0.0 -> NAN"),
        ("10.0 2.5\n", ("NUM", 4.0), "División normal 10.0 / 2.5 -> 4.0"),
        ("-10.0 2.5\n", ("NUM", -4.0), "División normal negativa -10.0 / 2.5 -> -4.0"),
    ],
    10: [
        ("0.0001\n", (99.3273, 100.0), "Acumulación de 0.0001 un millón de veces"),
        ("0.1\n", (100958.0, 100000.0), "Acumulación de 0.1 un millón de veces"),
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

def probar_reto(reto_num: int, ruta_cpp: str) -> bool:
    print(f"🔨 Probando Reto {reto_num} con: {ruta_cpp}")
    if not os.path.exists(ruta_cpp):
        print(f"❌ Archivo no encontrado: {ruta_cpp}")
        return False

    ruta_bin = compilar(ruta_cpp)
    exitos = 0
    casos = TEST_CASES[reto_num]
    
    try:
        for idx, (entrada, esperado, desc) in enumerate(casos, 1):
            try:
                salida = ejecutar_caso(ruta_bin, entrada)
                
                # Ejecutar validación específica
                if reto_num == 6:
                    ok, res = validar_reto6(salida)
                    if ok and res == esperado:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. Esperado: {esperado}, Obtenido: {res if ok else 'Error: ' + res}")
                elif reto_num == 7:
                    t_esp, r_esp, p_esp = esperado
                    ok, err = validar_reto7(salida, t_esp, r_esp, p_esp)
                    if ok:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. {err}")
                elif reto_num == 8:
                    ok, err = validar_reto8(salida, esperado)
                    if ok:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. {err}")
                elif reto_num == 9:
                    tipo, val = esperado
                    ok, err = validar_reto9(salida, tipo, val)
                    if ok:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. {err}")
                elif reto_num == 10:
                    f_esp, d_esp = esperado
                    ok, err = validar_reto10(salida, f_esp, d_esp)
                    if ok:
                        print(f"  [OK] Caso {idx}: {desc}")
                        exitos += 1
                    else:
                        print(f"  [FALLO] Caso {idx}: {desc}. {err}")

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
            print("❌ No se pudo determinar el número de reto del archivo. Especifica: test_dia_2.py <reto_num> <ruta_cpp>")
            sys.exit(1)

    if reto_num not in TEST_CASES:
        print(f"❌ Reto {reto_num} inválido para el Día 2.")
        sys.exit(1)

    exito = probar_reto(reto_num, ruta_cpp)
    sys.exit(0 if exito else 1)

if __name__ == "__main__":
    main()
