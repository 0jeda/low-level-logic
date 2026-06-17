# Día 2: Punto Flotante (`float` y `double`) e Imprecisión

## Teoría: La Ilusión de los Decimales (IEEE 754)

A diferencia de los enteros, los números decimales en los computadores se representan mediante el estándar **IEEE 754** (Punto Flotante). Se llaman de "punto flotante" porque la coma o punto decimal puede moverse (flotar) multiplicando el número por una potencia de 2, similar a la notación científica.

C++ tiene dos tipos principales:
* `float`: Precisión simple (4 bytes / 32 bits). Ofrece aproximadamente 7 dígitos significativos de precisión.
* `double`: Precisión doble (8 bytes / 64 bits). Ofrece aproximadamente 15-17 dígitos significativos.

### La Imprecisión Flotante
Como el computador trabaja en binario (base 2), no puede representar con exactitud fracciones que no sean potencias de 2. Por ejemplo, el número decimal `0.1` en binario es periódico:
$$0.1_{10} = 0.00011001100110011..._2$$

Como la memoria es finita, el computador debe **truncar o redondear** este valor periódico, introduciendo un pequeñísimo error de redondeo. Esto causa que operaciones simples como `0.1 + 0.2 == 0.3` devuelvan `false` en la máquina.

### Infinitos y NaN (Not a Number)
A diferencia de los enteros (donde dividir por cero aborta la ejecución del programa con un fallo), el estándar IEEE 754 define valores especiales para operaciones matemáticas inválidas o fuera de rango:
* `inf` y `-inf`: Infinito positivo y negativo (ej: `1.0 / 0.0`).
* `nan` / `NaN`: No es un Número (ej: `0.0 / 0.0` o `sqrt(-1)`).

---

## Retos del Día 2

### Reto 6: Comparación Flotante Segura
* **Archivo de plantilla:** `plantillas/reto_6.cpp`
* **Descripción:** Lee tres números de punto flotante `A`, `B` y `C` (`double`). Comprueba si la suma `A + B` es igual a `C`.
* **Regla:** Dado el error de precisión, no puedes compararlos directamente como `(A + B) == C`. Debes implementar una comparación usando un margen de error (tolerancia o épsilon) de $10^{-6}$ ($0.000001$).
* **Salida esperada:**
  - Si la diferencia absoluta entre `(A + B)` y `C` es menor o igual al épsilon: `IGUALES`
  - De lo contrario: `DIFERENTES`

### Reto 7: Truncamiento, Redondeo y Piso (Floor) a Mano
* **Archivo de plantilla:** `plantillas/reto_7.cpp`
* **Descripción:** Lee un número decimal `X` (`double`) que puede ser positivo o negativo. Escribe un programa que calcule y muestre:
  1. Su **truncamiento** (eliminar la parte decimal hacia cero).
  2. Su **redondeo al entero más cercano** (si la parte decimal es $\ge 0.5$ se redondea hacia arriba en magnitud, de lo contrario hacia abajo).
  3. Su **piso** (el mayor entero menor o igual a `X`).
* **Restricción:** No utilices la librería `<cmath>` ni funciones como `std::floor`, `std::round` o `std::trunc`. Debes hacerlo manualmente usando conversión de tipos (`cast` a `int`) y condicionales `if-else`.
* **Salida esperada:**
  ```text
  TRUNC=<valor>
  REDONDEO=<valor>
  PISO=<valor>
  ```

### Reto 8: Conversión de Temperatura (Fahrenheit a Celsius)
* **Archivo de plantilla:** `plantillas/reto_8.cpp`
* **Descripción:** Lee un valor decimal `F` (`double`) que representa grados Fahrenheit. Conviértelo a grados Celsius usando la fórmula:
  $$C = (F - 32) \times \frac{5}{9}$$
* **Peligro:** Si escribes `(F - 32) * (5 / 9)`, la expresión `5 / 9` se evaluará como división entera devolviendo `0`, arruinando el resultado. Debes asegurar que la división ocurra en punto flotante.
* **Salida esperada:**
  ```text
  C=<valor_en_celsius>
  ```

### Reto 9: Control de División por Cero Flotante
* **Archivo de plantilla:** `plantillas/reto_9.cpp`
* **Descripción:** Lee dos números decimales `A` y `B` (`double`). Realiza la división `A / B`. Si el divisor `B` es cero, detecta si el resultado es infinito positivo, infinito negativo, o no definido (NaN), y muestra el texto correspondiente sin que el programa aborte.
* **Regla:** 
  - Si `A > 0` y `B == 0`: Imprimir `INF`
  - Si `A < 0` y `B == 0`: Imprimir `-INF`
  - Si `A == 0` y `B == 0`: Imprimir `NAN`
  - De lo contrario: Imprimir el resultado de la división.
* **Salida esperada:**
  ```text
  RESULTADO=<INF | -INF | NAN | valor_decimal>
  ```

### Reto 10: Acumulación de Error de Precisión
* **Archivo de plantilla:** `plantillas/reto_10.cpp`
* **Descripción:** Lee un número flotante de precisión simple `X` (`float`), que típicamente será un valor pequeño como `0.0001`. En un bucle, súmalo a sí mismo 1,000,000 de veces (un millón) usando un acumulador de tipo `float` y, por separado, usando un acumulador de tipo `double`. Muestra la diferencia de precisión al final.
* **Salida esperada:**
  ```text
  FLOAT=<valor_final_con_float>
  DOUBLE=<valor_final_con_double>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_6.cpp soluciones/reto_6.cpp
# Edita soluciones/reto_6.cpp
python3 test_dia_2.py 6 soluciones/reto_6.cpp
```
O corre todas las soluciones completadas de hoy con:
```bash
python3 test_dia_2.py all
```
