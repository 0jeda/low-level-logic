# Día 4: Paso de Matrices (2D) a Funciones

## Teoría: Dirección de Memoria en Estructuras Multidimensionales

En C++, una matriz de dos dimensiones (2D) no es más que un bloque contiguo de memoria en el que las filas están dispuestas una tras otra (orden de fila principal o *Row-Major Order*).

Cuando pasamos una matriz a una función, a diferencia de los arreglos unidimensionales, **debemos indicar obligatoriamente el tamaño de todas las dimensiones excepto la primera**. Por ejemplo:

```cpp
void procesarMatriz(int mat[][50], int filas, int columnas);
```

### ¿Por qué es obligatoria la segunda dimensión?
Para poder acceder a `mat[i][j]`, el compilador de C++ necesita saber cuántos elementos hay por fila. La fórmula interna que calcula la dirección de memoria exacta del elemento en la fila `i`, columna `j` es:

$$\text{Dirección} = \text{Base} + (i \times \text{ColumnasDeclaradas} + j) \times \text{sizeof}(tipo)$$

Si el compilador no conoce el número de columnas de cada fila (`ColumnasDeclaradas`, en este caso 50), no puede calcular el salto de línea y la compilación fallará.

---

## Retos del Día 4

### Reto 121: Sumador de Matriz
* **Archivo de plantilla:** `plantillas/reto_121.cpp`
* **Descripción:** Lee las dimensiones `F` (filas) y `C` (columnas), y luego $F \times C$ enteros. Implementa `int sumarMatriz(const int mat[][50], int filas, int columnas)` que retorne la suma de todos los elementos de la matriz.
* **Salida esperada:**
  ```text
  SUMA=<suma_total>
  ```

### Reto 122: Visualizador de Matriz Formateada
* **Archivo de plantilla:** `plantillas/reto_122.cpp`
* **Descripción:** Lee `F` y `C`, seguidos de $F \times C$ enteros. Implementa `void imprimirMatriz(const int mat[][50], int filas, int columnas)` que imprima la matriz formateada fila por fila.
* **Salida esperada:**
  ```text
  FILA_0=[x00,x01,...,x0n]
  FILA_1=[x10,x11,...,x1n]
  ...
  ```

### Reto 123: Transposición de Matrices
* **Archivo de plantilla:** `plantillas/reto_123.cpp`
* **Descripción:** Lee `F` y `C`, y luego los enteros de la matriz. Implementa `void transponerMatriz(const int origen[][50], int filas, int columnas, int destino[][50])` que guarde la transpuesta de `origen` en `destino`. Imprime la matriz resultante en el formato del Reto 122.
* **Salida esperada:**
  ```text
  FILA_0=[x00,x10,...,xn0]
  FILA_1=[x01,x11,...,xn1]
  ...
  ```

### Reto 124: Suma de Matrices Modulares
* **Archivo de plantilla:** `plantillas/reto_124.cpp`
* **Descripción:** Lee `F` y `C`, y luego dos matrices de dimensiones $F \times C$ (matriz `A` y matriz `B`). Implementa `void sumarMatrices(const int A[][50], const int B[][50], int C[][50], int filas, int columnas)` que sume ambas matrices elemento por elemento en la matriz resultante `C`. Imprime la matriz `C` en el formato del Reto 122.
* **Salida esperada:**
  ```text
  FILA_0=[A00+B00,...]
  ...
  ```

### Reto 125: Copia Segura de Matrices
* **Archivo de plantilla:** `plantillas/reto_125.cpp`
* **Descripción:** Lee `F` y `C`, y los datos de una matriz. Implementa `void copiarMatriz(const int origen[][50], int destino[][50], int filas, int columnas)` que copie el contenido completo de `origen` a `destino`. Imprime la matriz `destino` en el formato del Reto 122.
* **Salida esperada:**
  ```text
  FILA_0=[x00,...]
  ...
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_121.cpp soluciones/reto_121.cpp
# Resuelve soluciones/reto_121.cpp
python3 test_dia_4.py soluciones/reto_121.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_4.py all
```
