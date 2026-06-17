# Día 5: Desplazamientos de Bits (`<<`, `>>`) y Máscaras

## Teoría: Movimiento de Bits

Los operadores de desplazamiento nos permiten desplazar los bits de un número hacia la izquierda o hacia la derecha. Son operaciones extremadamente rápidas a nivel de hardware.

### Desplazamiento a la Izquierda (`<<`)
Desplaza todos los bits hacia la izquierda `K` posiciones, rellenando con ceros por la derecha.
* Efecto matemático: Equivale a multiplicar el número por $2^K$.
* Ejemplo: `5 << 1` (5 es `101` en binario. Desplazado 1 es `1010` = 10 decimal).

### Desplazamiento a la Derecha (`>>`)
Desplaza todos los bits hacia la derecha `K` posiciones.
* Si el número es sin signo (`unsigned`), se rellena con ceros por la izquierda (desplazamiento lógico).
* Si el número es con signo (`signed`), el relleno depende de la implementación pero usualmente mantiene el bit de signo (desplazamiento aritmético).
* Efecto matemático: Equivale a realizar la división entera del número por $2^K$.
* Ejemplo: `10 >> 1` (10 es `1010`. Desplazado 1 es `0101` = 5 decimal).

---

## Retos del Día 5

### Reto 21: Aritmética de Desplazamientos
* **Archivo de plantilla:** `plantillas/reto_21.cpp`
* **Descripción:** Lee un entero con signo `N` y un exponente entero `K` ($K \ge 0$). Calcula la multiplicación $N \times 2^K$ y la división entera $N / 2^K$ utilizando únicamente operadores de desplazamiento de bits.
* **Restricción:** Quedan prohibidos los operadores `*` y `/`.
* **Salida esperada:**
  ```text
  MULT=<resultado_multiplicación>
  DIV=<resultado_división>
  ```

### Reto 22: Extractor de Bit P
* **Archivo de plantilla:** `plantillas/reto_22.cpp`
* **Descripción:** Lee un entero `N` y una posición `P` (0 a 31). Determina si el bit en la posición `P` está encendido (`1`) o apagado (`0`).
* **Pista:** Desplaza el número `P` posiciones a la derecha (`N >> P`) y haz un AND con `1` para aislar el bit, o usa una máscara.
* **Salida esperada:**
  ```text
  BIT=<0 | 1>
  ```

### Reto 23: Máscara de Rango Completo
* **Archivo de plantilla:** `plantillas/reto_23.cpp`
* **Descripción:** Lee dos índices de bit `L` y `R` ($0 \le L \le R \le 31$). Construye una máscara de 32 bits (un `unsigned int`) que tenga bits encendidos (`1`) únicamente en las posiciones desde `L` hasta `R` (ambos inclusive), e imprímela en decimal.
* **Ejemplo:** Si $L=2$ y $R=4$, los bits del 2 al 4 deben ser `1` (`...00011100` en binario), lo que equivale a $4 + 8 + 16 = 28$ en decimal.
* **Restricción:** No utilices bucles. Resuélvelo combinando desplazamientos y operaciones bitwise lógicas de forma constante $O(1)$. *Cuidado con el desbordamiento si el rango abarca los 32 bits.*
* **Salida esperada:**
  ```text
  MASCARA=<valor_decimal_de_la_mascara>
  ```

### Reto 24: Cuenta de Bits Encendidos en un Byte (Bucle)
* **Archivo de plantilla:** `plantillas/reto_24.cpp`
* **Descripción:** Lee un número de 8 bits sin signo `B` (un entero del `0` al `255`). Cuenta cuántos de sus bits están encendidos en `1` usando un bucle `while` o `for` que verifique bit a bit desplazando hacia la derecha.
* **Salida esperada:**
  ```text
  CANTIDAD=<número_de_bits_encendidos>
  ```

### Reto 25: Intercambiador de Nibbles (Nibble Swap)
* **Archivo de plantilla:** `plantillas/reto_25.cpp`
* **Descripción:** Un byte se compone de dos partes de 4 bits llamadas *nibbles* (el nibble alto son los bits 7-4, y el nibble bajo son los bits 3-0). Escribe un programa que lea un byte `B` (representado como entero `0` a `255`), intercambie de lugar su nibble alto con su nibble bajo, e imprima el valor entero resultante.
* **Ejemplo:** Si entra `100` (`0110 0100` en binario). Al intercambiar nibbles, queda `0100 0110` (que equivale a `70` en decimal).
* **Salida esperada:**
  ```text
  NUEVO=<valor_decimal_del_byte_modificado>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_21.cpp soluciones/reto_21.cpp
# Edita soluciones/reto_21.cpp
python3 test_dia_5.py 21 soluciones/reto_21.cpp
```
O prueba todas las soluciones completadas de hoy:
```bash
python3 test_dia_5.py all
```
