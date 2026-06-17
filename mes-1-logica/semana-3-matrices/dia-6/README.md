# Día 6: Ordenamiento In-Place en Matrices y Espacio Auxiliar

## Teoría: Mapeo Unidimensional para Ordenamiento 2D

Ordenar una matriz completa como si fuera un solo arreglo lineal suele resolverse copiando todos los elementos a un arreglo 1D auxiliar, ordenándolo, y volviéndolos a copiar a la matriz. Esto consume espacio de memoria **$O(R \times C)$**.

Sin embargo, podemos aplicar la **aritmética de Row-Major order a la inversa** para ordenar la matriz in-place sin gastar memoria adicional:

1. Consideramos que la matriz tiene un total de $M = R \times C$ elementos.
2. Cualquier índice lineal $k$ en el rango $[0, M - 1]$ se traduce a coordenadas bidimensionales de fila y columna mediante divisiones y módulos:
   $$\text{fila} = k / C$$
   $$\text{columna} = k \mathbin{\%} C$$
3. Podemos ejecutar Bubble Sort o Insertion Sort directamente usando este mapeo. Por ejemplo, al comparar el "índice lineal" $a$ y $b$, accedemos a `matriz[a/C][a%C]` y `matriz[b/C][b%C]`.

Esto nos permite ordenar celdas en un espacio auxiliar de **$O(1)$**.

---

## Retos del Día 6

### Reto 96: Ordenar una Matriz Completa In-Place
* **Archivo de plantilla:** `plantillas/reto_96.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Ordena todos sus elementos de forma ascendente como si fuera un único arreglo lineal, directamente en la matriz (in-place) con espacio auxiliar $O(1)$.
* **Salida esperada:**
  ```text
  MATRIZ=
  <fila_0_ordenada>
  ...
  ```

### Reto 97: Ordenar las Filas de una Matriz
* **Archivo de plantilla:** `plantillas/reto_97.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Ordena de forma independiente cada una de las filas de la matriz en orden ascendente usando Insertion Sort.
* **Salida esperada:**
  ```text
  MATRIZ=
  <fila_0_ordenada>
  ...
  ```

### Reto 98: Ordenar las Columnas de una Matriz
* **Archivo de plantilla:** `plantillas/reto_98.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Ordena de forma independiente cada una de las columnas de la matriz en orden ascendente usando Bubble Sort o Insertion Sort.
* **Salida esperada:**
  ```text
  MATRIZ=
  <fila_0_de_la_matriz_con_columnas_ordenadas>
  ...
  ```

### Reto 99: Ordenar la Diagonal Principal
* **Archivo de plantilla:** `plantillas/reto_99.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) y una matriz cuadrada de $N \times N$. Ordena ascendentemente los elementos situados en la diagonal principal in-place, dejando todos los demás elementos de la matriz en su lugar original.
* **Salida esperada:**
  ```text
  MATRIZ=
  <fila_0_con_diagonal_ordenada>
  ...
  ```

### Reto 100: Búsqueda Binaria en Matriz Totalmente Ordenada
* **Archivo de plantilla:** `plantillas/reto_100.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$), una matriz de $R \times C$ enteros **totalmente ordenada** (donde cada fila está ordenada de izquierda a derecha, y el primer elemento de la fila `i` es $\ge$ que el último de la fila `i-1`), y un objetivo `T`. Implementa Búsqueda Binaria en 2D mapeando el rango $[0, R \times C - 1]$ en tiempo **$O(\log(R \times C))$**.
* **Salida esperada:**
  - Si se encuentra: `POSICION=(<fila>,<columna>)`
  - Si no: `ERROR`

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_96.cpp soluciones/reto_96.cpp
# Resuelve soluciones/reto_96.cpp
python3 test_dia_6.py 96 soluciones/reto_96.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_6.py all
```
