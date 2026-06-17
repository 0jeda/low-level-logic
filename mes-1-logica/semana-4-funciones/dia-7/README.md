# Día 7: Proyecto Integrador - Calculadora de Álgebra Lineal

## Teoría: Integración de Conceptos Modulares

Hoy consolidarás todos los conceptos aprendidos durante la semana:
1. **Modularidad:** Dividir un problema complejo en subfunciones con responsabilidades únicas y acotadas.
2. **Paso de Parámetros Eficiente:** Pasar matrices por referencia para evitar la copia innecesaria de memoria y punteros de solo lectura (`const`).
3. **Validación de Reglas Matemáticas:** Controlar el flujo del programa basándose en las dimensiones requeridas para cada operación de álgebra lineal.

---

## Estructura del Proyecto

Implementarás las cuatro operaciones fundamentales de matrices paso a paso en retos individuales, y finalmente construirás un programa integrador que use todos estos bloques modulares en una mini-calculadora comandada por consola.

Todas las matrices tendrán un tamaño máximo declarado de `50x50`, pero se trabajará dinámicamente con las filas (`F`) y columnas (`C`) proporcionadas por el usuario.

---

## Retos del Día 7

### Reto 136: Suma de Matrices (Módulo)
* **Archivo de plantilla:** `plantillas/reto_136.cpp`
* **Descripción:** Lee `F` y `C`, luego la matriz `A` y la matriz `B`. Implementa la función `void sumarMatrices(const int A[][50], const int B[][50], int R[][50], int filas, int columnas)` e imprime el resultado.
* **Salida esperada:**
  ```text
  FILA_0=[x00,x01,...]
  ...
  ```

### Reto 137: Resta de Matrices (Módulo)
* **Archivo de plantilla:** `plantillas/reto_137.cpp`
* **Descripción:** Lee `F` y `C`, luego la matriz `A` y la matriz `B`. Implementa la función `void restarMatrices(const int A[][50], const int B[][50], int R[][50], int filas, int columnas)` e imprime la matriz resultante `A - B`.
* **Salida esperada:**
  ```text
  FILA_0=[x00,x01,...]
  ...
  ```

### Reto 138: Multiplicación de Matrices (Módulo)
* **Archivo de plantilla:** `plantillas/reto_138.cpp`
* **Descripción:** Lee las dimensiones `F_A` y `C_A`, luego la matriz `A`. A continuación lee `F_B` y `C_B`, y la matriz `B`. 
* Implementa la función `void multiplicarMatrices(const int A[][50], const int B[][50], int R[][50], int filas_A, int cols_A, int cols_B)`.
* **Salida esperada:** La matriz resultante de dimensiones $F_A \times C_B$ en formato `FILA_i=[...]`.

### Reto 139: Traza de una Matriz Cuadrada (Módulo)
* **Archivo de plantilla:** `plantillas/reto_139.cpp`
* **Descripción:** Lee el tamaño `N` para una matriz cuadrada de $N \times N$, y luego los elementos de la matriz. Implementa la función `int calcularTraza(const int A[][50], int n)` que sume los elementos de la diagonal principal ($A_{00} + A_{11} + \dots + A_{nn}$).
* **Salida esperada:**
  ```text
  TRAZA=<resultado>
  ```

### Reto 140: Calculadora de Álgebra Lineal Integradora
* **Archivo de plantilla:** `plantillas/reto_140.cpp`
* **Descripción:** Lee un carácter de operación: `+` (suma), `-` (resta), `*` (multiplicación) o `T` (traza).
  * Si es `+` o `-`: Lee `F C`, luego las matrices `A` y `B`. Ejecuta e imprime la matriz resultante.
  * Si es `*`: Lee `F_A C_A`, la matriz `A`, luego `F_B C_B` y la matriz `B`. Si `C_A != F_B`, imprime `ERROR_DIMENSION` y finaliza. Si es válido, ejecuta la multiplicación e imprime la matriz resultante.
  * Si es `T`: Lee `N` y la matriz `A`. Ejecuta e imprime `TRAZA=<resultado>`.
* **Salida esperada:** Según la operación seleccionada (siguiendo el formato de los retos 136 a 139) o `ERROR_DIMENSION`.

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_136.cpp soluciones/reto_136.cpp
# Resuelve soluciones/reto_136.cpp
python3 test_dia_7.py soluciones/reto_136.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_7.py all
```
