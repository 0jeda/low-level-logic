# Día 2: Diagonales de Matrices, Espirales y Rotaciones

## Teoría: Recorridos No Estándar e In-Place

Una vez dominados los recorridos secuenciales (por filas y por columnas), el siguiente paso es manipular las celdas siguiendo patrones geométricos y espaciales más complejos.

### 1. Las Diagonales en Matrices Cuadradas ($N \times N$)
* **Diagonal Principal:** Conecta la esquina superior izquierda con la inferior derecha. Se caracteriza porque los índices de fila y columna son idénticos:
  $$\text{Condición: } i == j$$
* **Diagonal Secundaria:** Conecta la esquina superior derecha con la inferior izquierda. Se caracteriza porque la suma de sus índices es constante:
  $$\text{Condición: } i + j == N - 1$$

### 2. Rotación de Matrices de forma In-Place ($O(1)$ Espacio Auxiliar)
Rotar una imagen o grilla 90 grados es una operación común en procesamiento gráfico y desarrollo de videojuegos. Si usamos una matriz auxiliar para copiar los elementos a su nueva posición, consumimos espacio extra $O(N^2)$.

Sin embargo, podemos lograr una rotación de **90 grados a la derecha (sentido horario)** directamente sobre la misma memoria (in-place) mediante dos pasos algebraicos:
1. **Transponer la matriz:** Intercambiar celdas $A[i][j]$ con $A[j][i]$ para toda celda por encima de la diagonal principal ($j > i$).
2. **Invertir horizontalmente cada fila:** Invertir los elementos de cada fila por separado.

Este ingenioso truco reduce la complejidad espacial auxiliar a un estricto **$O(1)$**.

---

## Retos del Día 2

### Reto 76: Suma de Diagonales de Matriz Cuadrada
* **Archivo de plantilla:** `plantillas/reto_76.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) y una matriz cuadrada de $N \times N$. Calcula la suma de la diagonal principal, la suma de la diagonal secundaria, y determina si ambas sumas coinciden.
* **Salida esperada:**
  ```text
  PRINCIPAL=<suma_principal>
  SECUNDARIA=<suma_secundaria>
  IGUALES=<SI | NO>
  ```

### Reto 77: Recorrido en Espiral
* **Archivo de plantilla:** `plantillas/reto_77.cpp`
* **Descripción:** Lee dos enteros `R` y `C` ($1 \le R, C \le 50$) y una matriz de $R \times C$ enteros. Imprime los elementos de la matriz en orden espiral, comenzando desde la celda superior izquierda `(0,0)`, yendo a la derecha hasta el final, luego abajo, luego izquierda, luego arriba, y volviendo a repetir el patrón en espiral hacia adentro.
* **Salida esperada (elementos separados por un espacio):**
  ```text
  ESPIRAL=<e1> <e2> ... <e_RxC>
  ```

### Reto 78: Rotar Matriz 90 Grados a la Derecha In-Place
* **Archivo de plantilla:** `plantillas/reto_78.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) y una matriz cuadrada de $N \times N$. Rota la matriz 90 grados a la derecha de forma cíclica.
* **Restricción:** Está prohibido declarar una segunda matriz auxiliar. Debes realizar la rotación en la misma memoria física mediante transposición e inversión de filas.
* **Salida esperada:**
  ```text
  ROTADA=
  <fila_0_de_la_matriz_rotada>
  ...
  ```

### Reto 79: Validador de Matriz Identidad
* **Archivo de plantilla:** `plantillas/reto_79.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) y una matriz cuadrada de $N \times N$. Determina si la matriz es la **Matriz Identidad** (todos los elementos de la diagonal principal son `1` y todos los demás elementos fuera de ella son `0`).
* **Salida esperada:**
  ```text
  IDENTIDAD=<SI | NO>
  ```

### Reto 80: Espejo Horizontal In-Place
* **Archivo de plantilla:** `plantillas/reto_80.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y una matriz de $R \times C$ enteros. Invierte horizontalmente cada una de las filas de la matriz directamente sobre su memoria (in-place).
* **Salida esperada:**
  ```text
  ESPEJO=
  <fila_0_espejada>
  ...
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_76.cpp soluciones/reto_76.cpp
# Resuelve soluciones/reto_76.cpp
python3 test_dia_2.py 76 soluciones/reto_76.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_2.py all
```
