# Día 5: Búsqueda y Sumas en Matrices Especiales

## Teoría: Algoritmos Eficientes sobre Matrices Especiales

No todas las matrices contienen datos desordenados y aleatorios. En muchos problemas matemáticos y de ingeniería de datos, las matrices poseen propiedades estructuradas que nos permiten diseñar algoritmos especializados extremadamente rápidos.

### 1. Búsqueda en Matriz Ordenada 2D (Stepwise Search)
Imagina una matriz donde **cada fila está ordenada de izquierda a derecha** y **cada columna está ordenada de arriba a abajo**:
$$\begin{pmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 27 & 29 & 37 \end{pmatrix}$$
Si buscamos un elemento `T = 29` usando fuerza bruta, tardamos tiempo $O(R \times C)$ inspeccionando todas las celdas.

Sin embargo, podemos iniciar en la **esquina superior derecha (fila 0, columna C-1)**:
* Si el elemento actual es igual a `T`, terminamos.
* Si es mayor que `T` (ej: 30 > 29), toda esa columna hacia abajo debe ser mayor que `T`. Descartamos la columna moviéndonos a la izquierda: `col--`.
* Si es menor que `T` (ej: 20 < 29), toda esa fila hacia la izquierda debe ser menor que `T`. Descartamos la fila moviéndonos hacia abajo: `fila++`.

Este método en "escalera" reduce el tiempo de búsqueda a un estricto **$O(R + C)$**.

### 2. Prefix Sum Bidimensional (Suma de Submatrices en $O(1)$)
Para responder a la suma de cualquier submatriz delimitada por `(r1, c1)` (arriba-izquierda) y `(r2, c2)` (abajo-derecha), precalculamos una matriz de suma acumulada en 2D:
$$\text{pref}[i][j] = \text{mat}[i][j] + \text{pref}[i-1][j] + \text{pref}[i][j-1] - \text{pref}[i-1][j-1]$$
Una vez precalculada, cualquier consulta de suma se responde en **$O(1)$**:
$$\text{Suma} = \text{pref}[r2][c2] - \text{pref}[r1-1][c2] - \text{pref}[r2][c1-1] + \text{pref}[r1-1][c1-1]$$

---

## Retos del Día 5

### Reto 91: Búsqueda en Matriz Ordenada 2D (Stepwise Search)
* **Archivo de plantilla:** `plantillas/reto_91.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$), la matriz de $R \times C$ enteros (garantizada de estar ordenada por filas y columnas), y un objetivo `T`. Encuentra la primera posición `(fila, columna)` de `T` en la matriz usando búsqueda en escalera en tiempo $O(R + C)$.
* **Salida esperada:**
  - Si se encuentra: `POSICION=(<fila>,<columna>)`
  - Si no: `ERROR`

### Reto 92: Fila con Más Ceros
* **Archivo de plantilla:** `plantillas/reto_92.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y una matriz binaria (solo `0`s y `1`s) de $R \times C$, donde cada fila está ordenada (lo que significa que todos los `0`s preceden a los `1`s). Encuentra la fila (0-indexada) que contenga la mayor cantidad de ceros en tiempo $O(R + C)$ o $O(R \log C)$.
* **Salida esperada:**
  ```text
  FILA=<fila>
  ```

### Reto 93: Suma de Submatriz en Tiempo Constante
* **Archivo de plantilla:** `plantillas/reto_93.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$), la matriz de $R \times C$ enteros, y el número de consultas `Q` ($1 \le Q \le 10$). Cada consulta consiste en cuatro índices: `r1 c1 r2 c2` ($0 \le r1 \le r2 < R$, $0 \le c1 \le c2 < C$).
* **Objetivo:** Precalcula la matriz de sumas acumuladas en 2D en $O(R \times C)$ para responder cada una de las consultas de suma de submatriz en tiempo constante $O(1)$.
* **Salida esperada (una línea por consulta):**
  ```text
  SUMA=<resultado>
  ```

### Reto 94: Multiplicación de Matriz por Vector
* **Archivo de plantilla:** `plantillas/reto_94.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$), la matriz de $R \times C$ enteros, y un vector (arreglo 1D) de tamaño `C`. Realiza el producto matricial $M \times V$ y muestra el vector resultante de tamaño `R`.
* **Salida esperada (elementos separados por un espacio):**
  ```text
  VECTOR=<v1> <v2> ... <vR>
  ```

### Reto 95: Puntos de Silla (Saddle Point)
* **Archivo de plantilla:** `plantillas/reto_95.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y la matriz de $R \times C$ enteros. Encuentra un **punto de silla** en la matriz. Un elemento es un punto de silla si es el **mínimo** de su fila y, al mismo tiempo, el **máximo** de su columna.
* **Salida esperada:**
  - Si existe: `SILLA=<valor> EN (<fila>,<columna>)`
  - Si no existe: `NINGUNO`

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_91.cpp soluciones/reto_91.cpp
# Resuelve soluciones/reto_91.cpp
python3 test_dia_5.py 91 soluciones/reto_91.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_5.py all
```
