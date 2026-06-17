# Día 1: Matrices en Memoria Contigua y Recorridos Básicos

## Teoría: La Ilusión Bidimensional en Hardware

Las matrices (arreglos 2D) nos permiten modelar grillas, imágenes y sistemas de coordenadas de forma intuitiva. Sin embargo, en el hardware de la computadora, **toda la memoria es lineal y secuencial**.

### Representación por Fila (Row-Major Order)
C++ organiza las matrices por defecto en **Row-Major Order**. Esto significa que las filas se almacenan completas una detrás de la otra de forma consecutiva en la memoria RAM:

Para una matriz conceptual de $3 \times 3$:
$$\begin{pmatrix} a_{00} & a_{01} & a_{02} \\ a_{10} & a_{11} & a_{12} \\ a_{20} & a_{21} & a_{22} \end{pmatrix}$$

El compilador de C++ la acomoda linealmente en memoria como:
```text
Dirección: [ 0 ]  [ 1 ]  [ 2 ]  [ 3 ]  [ 4 ]  [ 5 ]  [ 6 ]  [ 7 ]  [ 8 ]
Elemento:  a00    a01    a02    a10    a11    a12    a20    a21    a22
          |--- Fila 0 --------| |--- Fila 1 --------| |--- Fila 2 --------|
```

Para acceder al elemento en la fila $i$ y columna $j$ en una matriz de $C$ columnas totales, la CPU calcula la posición física en el arreglo lineal unidimensional mediante:
$$\text{Índice 1D} = (i \times C) + j$$

Dominar este cálculo de índices permite optimizar recorridos de matrices de forma secuencial y comprender la optimización de cachés de la CPU.

---

## Retos del Día 1

### Reto 71: Suma de Filas y Columnas
* **Archivo de plantilla:** `plantillas/reto_71.cpp`
* **Descripción:** Lee dos enteros `R` (filas) y `C` (columnas) ($1 \le R, C \le 50$), seguidos de los $R \times C$ enteros que componen la matriz. Calcula e imprime la suma de cada fila (en una sola línea) y la suma de cada columna (en la siguiente línea).
* **Salida esperada:**
  ```text
  FILAS=<sumaF0> <sumaF1> ... <sumaFR-1>
  COLUMNAS=<sumaC0> <sumaC1> ... <sumaCC-1>
  ```

### Reto 72: Aritmética de Índices 1D
* **Archivo de plantilla:** `plantillas/reto_72.cpp`
* **Descripción:** Lee dos enteros `R` y `C` ($1 \le R, C \le 50$), seguidos de la matriz de $R \times C$ enteros. Finalmente lee las coordenadas de celda `i` (fila) y `j` (columna).
* **Objetivo:** Calcula manualmente el índice lineal unidimensional (`i * C + j`) que corresponde a esa posición e imprime el valor de la celda. Si `i` o `j` están fuera de los límites de la matriz, muestra un mensaje de error.
* **Salida esperada:**
  - Si es válido:
    ```text
    INDICE1D=<indice_calculado>
    VALOR=<valor_celda>
    ```
  - Si es inválido: `ERROR`

### Reto 73: Matriz Transpuesta
* **Archivo de plantilla:** `plantillas/reto_73.cpp`
* **Descripción:** Lee dos enteros `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Genera e imprime su matriz transpuesta (de tamaño $C \times R$), donde las filas de la matriz original se convierten en columnas y viceversa.
* **Salida esperada:**
  ```text
  TRANSPUESTA=
  <fila_0_de_la_transpuesta>
  <fila_1_de_la_transpuesta>
  ...
  ```

### Reto 74: Máximo y Mínimo en Matriz con Coordenadas
* **Archivo de plantilla:** `plantillas/reto_74.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Encuentra el elemento de mayor valor (máximo) y el de menor valor (mínimo) junto con sus coordenadas de fila y columna (0-indexadas).
* **Regla:** Si hay valores repetidos del máximo o mínimo, selecciona el primero que aparezca en el recorrido por filas (Row-Major).
* **Salida esperada:**
  ```text
  MAX=<valor> EN (<fila>,<columna>)
  MIN=<valor> EN (<fila>,<columna>)
  ```

### Reto 75: Comprobar Matriz Simétrica
* **Archivo de plantilla:** `plantillas/reto_75.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) que representa el tamaño de una matriz cuadrada de $N \times N$, seguido de sus elementos. Determina si la matriz es simétrica respecto a su diagonal principal (es decir, si la matriz es idéntica a su transpuesta: $A[i][j] == A[j][i]$ para todo $0 \le i, j < N$).
* **Salida esperada:**
  ```text
  SIMETRICA=<SI | NO>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_71.cpp soluciones/reto_71.cpp
# Resuelve soluciones/reto_71.cpp
python3 test_dia_1.py 71 soluciones/reto_71.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_1.py all
```
