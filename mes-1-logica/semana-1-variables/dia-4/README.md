# Día 4: Operadores a Nivel de Bits Básicos (`&`, `|`, `^`, `~`)

## Teoría: Pensar en Binario

Bajo el capó, el computador no entiende números decimales ni letras; entiende únicamente **ceros y unos (bits)**. Cada tipo de dato entero está compuesto por un conjunto de bits (un `int` son 32 bits).

C++ nos permite manipular estos bits individualmente mediante los **operadores a nivel de bits (bitwise operators)**:

| Operador | Nombre | Operación |
| :--- | :--- | :--- |
| `&` | AND | Da `1` sólo si ambos bits son `1`. |
| `\|` | OR | Da `1` si al menos uno de los bits es `1`. |
| `^` | XOR | Da `1` si los bits son diferentes (uno `1` y el otro `0`). |
| `~` | NOT | Invierte todos los bits (los `0` se vuelven `1` y viceversa). |

### Tablas de Verdad Bitwise
Si operamos dos bits $x$ e $y$:
* $x \mathbin{\&} y$: Filtrar o apagar bits (máscara).
* $x \mathbin{|} y$: Encender bits.
* $x \mathbin{\wedge} y$: Conmutar o alternar bits.
* $\mathord{\sim}x$: Negar (Complemento a uno).

---

## Retos del Día 4

### Reto 16: Par o Impar Binario
* **Archivo de plantilla:** `plantillas/reto_16.cpp`
* **Descripción:** Lee un número entero `N` y determina si es par o impar.
* **Restricción:** Queda **estrictamente prohibido** usar el operador módulo `%` (ej. `N % 2`). Debes resolverlo utilizando únicamente el operador a nivel de bits `&` para verificar el bit de menor peso (el bit en la posición 0).
* **Salida esperada:**
  ```text
  PAR   (si es par)
  IMPAR (si es impar)
  ```

### Reto 17: El Intercambio XOR (Bitwise Swap)
* **Archivo de plantilla:** `plantillas/reto_17.cpp`
* **Descripción:** Lee dos números enteros `A` y `B` e intercambia sus valores.
* **Restricción:** No uses variables auxiliares ni operaciones aritméticas (`+` o `-`). Debes resolverlo aplicando el operador `^` (XOR) tres veces sobre `A` y `B`.
* **Salida esperada:**
  ```text
  A=<nuevo_A>
  B=<nuevo_B>
  ```

### Reto 18: Apagar Bit en la Posición P
* **Archivo de plantilla:** `plantillas/reto_18.cpp`
* **Descripción:** Lee un entero `N` y una posición de bit `P` (entre 0 y 31). Apaga el bit que está en la posición `P` de la representación binaria de `N` (ponlo en `0`) sin alterar los demás bits, e imprime el valor resultante.
* **Pista:** Usa una máscara construida con el operador de desplazamiento a la izquierda (`1 << P`) y luego niégala (`~`) para usarla con un `&`.
* **Salida esperada:**
  ```text
  RESULTADO=<nuevo_valor>
  ```

### Reto 19: Encender Bit en la Posición P
* **Archivo de plantilla:** `plantillas/reto_19.cpp`
* **Descripción:** Lee un entero `N` y una posición de bit `P` (entre 0 y 31). Enciende el bit que está en la posición `P` de `N` (ponlo en `1`), manteniendo todos los demás bits sin cambios, e imprime el número resultante.
* **Salida esperada:**
  ```text
  RESULTADO=<nuevo_valor>
  ```

### Reto 20: El Secreto del Complemento a Dos
* **Archivo de plantilla:** `plantillas/reto_20.cpp`
* **Descripción:** Lee un número entero con signo `N`. Aplica el operador de negación bitwise `~N` y guárdalo en una variable. Luego, suma 1 a esa variable. Muestra ambos valores por consola.
* **Objetivo:** Comprender experimentalmente por qué invertir todos los bits y sumar uno (`~N + 1`) es igual a multiplicar el número por $-1$ (la representación de números negativos bajo el Complemento a Dos).
* **Salida esperada:**
  ```text
  NOT=<valor_de_tilde_N>
  NEG=<valor_de_tilde_N_mas_uno>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_16.cpp soluciones/reto_16.cpp
# Edita soluciones/reto_16.cpp
python3 test_dia_4.py 16 soluciones/reto_16.cpp
```
O prueba todos los retos del Día 4 que hayas implementado:
```bash
python3 test_dia_4.py all
```
