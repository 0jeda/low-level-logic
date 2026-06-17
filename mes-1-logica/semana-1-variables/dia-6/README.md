# Día 6: Práctica Integrada de Bits y Tipos

## Teoría: Serialización y Manipulación Avanzada

Una de las aplicaciones más potentes de la manipulación de bits es la **compactación de datos** y el **desempaquetado de protocolos de red o archivos binarios**. 

### Empaquetado de Datos (Bit Packing)
Imagina que necesitas enviar 4 caracteres ASCII (`char`) por una red de comunicación. Cada `char` ocupa 1 byte (8 bits). Si los envías individualmente, realizas 4 envíos. Pero un entero estándar (`int`) ocupa 4 bytes (32 bits). Podemos usar desplazamientos y el operador OR (`|`) para empaquetar los 4 caracteres dentro de un solo entero y transmitirlo todo junto:
```text
Byte 3 (MSB)   Byte 2          Byte 1          Byte 0 (LSB)
[ Carácter 1 ] [ Carácter 2 ] [ Carácter 3 ] [ Carácter 4 ]
```
Esto se logra desplazando cada byte a su posición correspondiente y combinándolos con OR:
```cpp
unsigned int empaquetado = (c1 << 24) | (c2 << 16) | (c3 << 8) | c4;
```

### El Peligro del Comportamiento Indefinido (Undefined Behavior)
En C++, intentar desplazar un tipo de dato de 32 bits por 32 o más posiciones (ej: `A >> 32`) resulta en un **Comportamiento Indefinido**. La CPU física puede hacer cosas extrañas (como no desplazar nada o fallar), por lo que debemos ser muy cuidadosos y añadir protecciones o modularizar los desplazamientos.

---

## Retos del Día 6

### Reto 26: Empaquetar 4 Caracteres en un Entero de 32 bits
* **Archivo de plantilla:** `plantillas/reto_26.cpp`
* **Descripción:** Lee 4 caracteres `C1`, `C2`, `C3` y `C4` desde la entrada estándar. Empaquétalos dentro de un único entero de 32 bits sin signo (`unsigned int`) en ese orden: `C1` en los 8 bits más significativos (MSB) y `C4` en los 8 bits menos significativos (LSB). Muestra el entero resultante en decimal.
* **Salida esperada:**
  ```text
  ENTERO=<valor_decimal_del_empaquetado>
  ```

### Reto 27: Desempaquetar 4 Caracteres
* **Archivo de plantilla:** `plantillas/reto_27.cpp`
* **Descripción:** Lee un número entero de 32 bits sin signo (`unsigned int` N) que contiene 4 caracteres empaquetados. Desempaqueta y extrae los 4 caracteres en su orden original e imprímelos en consola separados por un espacio.
* **Pista:** Usa desplazamientos a la derecha para posicionar los bits deseados al principio, y luego aplica una máscara `0xFF` para aislar ese carácter.
* **Salida esperada:**
  ```text
  CHARS=<c1> <c2> <c3> <c4>
  ```

### Reto 28: Rotación Circular de Bits (Shift Circular)
* **Archivo de plantilla:** `plantillas/reto_28.cpp`
* **Descripción:** Lee un entero sin signo de 32 bits `N` y una cantidad de rotación `R` ($0 \le R \le 31$). Realiza una **rotación circular hacia la izquierda** de `N` en `R` posiciones (los bits que salen por la izquierda deben entrar por la derecha).
* **Precaución extrema:** Si $R = 0$, la operación `32 - R` será `32`, y desplazar 32 posiciones causará *Comportamiento Indefinido*. Debes manejar este caso borde de forma segura.
* **Salida esperada:**
  ```text
  ROTADO=<valor_rotado_en_decimal>
  ```

### Reto 29: Palíndromo Binario en un Byte
* **Archivo de plantilla:** `plantillas/reto_29.cpp`
* **Descripción:** Lee un byte `B` (entero sin signo del `0` al `255`). Determina si su representación binaria de 8 bits es simétrica (es un palíndromo).
* **Ejemplo:** `129` en binario es `10000001`, que se lee igual al derecho y al revés. `100` en binario es `01100100`, que al revés es `00100110` (no es simétrico).
* **Salida esperada:**
  ```text
  PALINDROMO=<ES_PALINDROMO | NO_ES_PALINDROMO>
  ```

### Reto 30: Sumar 1 sin usar Aritmética Directa (Ripple Carry)
* **Archivo de plantilla:** `plantillas/reto_30.cpp`
* **Descripción:** Lee un número entero `N`. Súmale `1` a su valor actual y muestra el resultado.
* **Restricción:** Está **estrictamente prohibido** usar el operador de suma `+`, resta `-`, incremento `++`, o decremento `--`. Debes hacerlo utilizando únicamente operadores a nivel de bits y un bucle para simular el comportamiento de un sumador binario con acarreo (*Half-Adder* en cascada).
* **Pista:** Invierte los bits de `N` comenzando desde el bit menos significativo hacia la izquierda mientras encuentres bits en `1`. En el primer bit en `0` que encuentres, conviértelo a `1` y detente.
* **Salida esperada:**
  ```text
  RESULTADO=<nuevo_valor>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_26.cpp soluciones/reto_26.cpp
# Edita soluciones/reto_26.cpp
python3 test_dia_6.py 26 soluciones/reto_26.cpp
```
O prueba todas las soluciones completadas de hoy:
```bash
python3 test_dia_6.py all
```
