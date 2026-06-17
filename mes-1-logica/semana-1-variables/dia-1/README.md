# Día 1: Enteros, Límites y Desbordamientos (Overflow)

## Teoría: La Realidad de los Enteros en Memoria

En la programación académica tradicional, solemos pensar en los números como entidades abstractas e infinitas. En los sistemas reales, **los números son finitos y ocupan un espacio físico en memoria medido en bytes**.

C++ nos permite elegir la precisión y el tipo de representación (con o sin signo) de nuestros enteros:

| Tipo | Tamaño típico | Rango de valores aproximado | Formato de lectura/escritura |
| :--- | :--- | :--- | :--- |
| `short` | 2 bytes (16 bits) | $-32,768$ a $32,767$ | `%hd` / `short` |
| `int` | 4 bytes (32 bits) | $-2.14 \times 10^9$ a $2.14 \times 10^9$ | `%d` / `int` |
| `long long` | 8 bytes (64 bits) | $-9.22 \times 10^{18}$ a $9.22 \times 10^{18}$ | `%lld` / `long long` |
| `unsigned int` | 4 bytes (32 bits) | $0$ a $4,294,967,295$ | `%u` / `unsigned` |

### ¿Qué es el desbordamiento (Overflow)?
Cuando intentas almacenar un número que excede el límite del tipo de dato, los bits de mayor peso se pierden o el bit de signo se altera. 
* Con **enteros sin signo (`unsigned`)**, el desbordamiento está definido por el estándar como aritmética modular (da la vuelta a `0` si sumas 1 al valor máximo).
* Con **enteros con signo (`signed`)**, el desbordamiento es un comportamiento indefinido (*Undefined Behavior* o *UB*) en C++, pero comúnmente en arquitecturas modernas de complemento a dos, da la vuelta al valor mínimo negativo.

---

## Retos del Día 1

### Reto 1: El Intercambio de Variables (Aritmético)
* **Archivo de plantilla:** `plantillas/reto_1.cpp`
* **Descripción:** Lee dos números enteros `A` y `B` desde la entrada estándar e intercambia sus valores.
* **Restricción:** No uses variables auxiliares. Resuélvelo usando únicamente sumas y restas sobre `A` y `B`.
* **Salida esperada:**
  ```text
  A=<nuevo_valor_A>
  B=<nuevo_valor_B>
  ```

### Reto 2: Suma Segura (Prevenir Overflow)
* **Archivo de plantilla:** `plantillas/reto_2.cpp`
* **Descripción:** Lee dos enteros de 32 bits con signo (`int`), `A` y `B`. Antes de sumarlos, determina si la operación causará un desbordamiento por exceso (Overflow) o por defecto (Underflow).
* **Regla:** Está prohibido sumarlos en una variable de mayor tamaño (como `long long`) para validar el desbordamiento. Tienes que detectarlo usando lógica algebraica antes de realizar la suma sobre los mismos `int`.
* **Salida esperada:**
  - Si hay desbordamiento positivo: `OVERFLOW`
  - Si hay desbordamiento negativo: `UNDERFLOW`
  - Si la suma es segura: Imprimir el resultado de `A + B`.

### Reto 3: Conversión con Pérdida (Truncamiento de Bits)
* **Archivo de plantilla:** `plantillas/reto_3.cpp`
* **Descripción:** Lee un número entero de 64 bits (`long long` A) e imprímelo convertido explícitamente mediante cast a un `int` (32 bits) y a un `short` (16 bits).
* **Objetivo:** Comprender visualmente cómo se pierden los bits más significativos al forzar un tipo de dato más pequeño.
* **Salida esperada:**
  ```text
  INT=<valor_convertido_a_int>
  SHORT=<valor_convertido_a_short>
  ```

### Reto 4: Multiplicación de Precisión
* **Archivo de plantilla:** `plantillas/reto_4.cpp`
* **Descripción:** Lee dos enteros con signo de 32 bits (`int`), `A` y `B`. Calcula su multiplicación exacta y guárdala en un `long long`.
* **Advertencia:** Si haces `long long res = A * B;` directamente, el compilador multiplicará `A` y `B` como `int` de 32 bits (lo que puede desbordarse) y luego guardará el resultado corrupto en el `long long`. Debes forzar a que la multiplicación ocurra en 64 bits usando casting.
* **Salida esperada:**
  ```text
  PRODUCTO=<resultado_exacto_64_bits>
  ```

### Reto 5: Préstamo y Vuelta en Unsigned (Underflow)
* **Archivo de plantilla:** `plantillas/reto_5.cpp`
* **Descripción:** Lee dos enteros sin signo de 32 bits (`unsigned int`), `A` y `B`. Resta `A - B`.
* **Objetivo:** Ver qué sucede cuando `A < B` en aritmética sin signo.
* **Salida esperada:**
  ```text
  RESULTADO=<valor_de_A_menos_B>
  ```

---

## Cómo Ejecutar las Pruebas

Copia la plantilla correspondiente a la carpeta `soluciones/` y escribe tu solución. Por ejemplo, para el Reto 1:
```bash
cp plantillas/reto_1.cpp soluciones/reto_1.cpp
# Edita soluciones/reto_1.cpp
python3 test_dia_1.py 1 soluciones/reto_1.cpp
```
Para probar todos los retos del día que tengas creados:
```bash
python3 test_dia_1.py all
```
