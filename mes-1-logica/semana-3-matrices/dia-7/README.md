# Día 7: El Gran Reto Semanal y Git de Matrices

## Teoría: Simulación Física y Motores de Juegos en Consola

Hoy concluimos la tercera semana. A estas alturas, ya dominas la manipulación espacial de las matrices 2D, el ordenamiento in-place y la aritmética de celdas.

Las matrices no solo sirven para almacenar tablas de base de datos; son la representación estándar de los **tableros de juego (grids)** y motores de simulación.

### Simulación de Vecindades en una Grilla
En juegos como Buscaminas o en simulaciones físicas como el *Juego de la Vida de Conway*, cada celda se ve afectada por el estado de sus **8 vecinos contiguos** (arriba, abajo, izquierda, derecha y las 4 diagonales).

Para verificar los vecinos de forma segura sin provocar desbordamientos de memoria (acceso a índices fuera de límites de la matriz como `fila - 1 < 0`), debemos usar condicionales protectores en cada verificación o declarar un arreglo de desplazamientos relativos:
```cpp
int dRow[] = {-1, -1, -1,  0, 0,  1,  1, 1};
int dCol[] = {-1,  0,  1, -1, 1, -1,  0, 1};

for (int k = 0; k < 8; ++k) {
    int nRow = fila + dRow[k];
    int nCol = col + dCol[k];
    if (nRow >= 0 && nRow < R && nCol >= 0 && nCol < C) {
        // Acceso seguro a la celda vecina matriz[nRow][nCol]
    }
}
```

---

## Retos del Día 7

### Reto 101: Tablero de Buscaminas (Vecindad de Minas)
* **Archivo de plantilla:** `plantillas/reto_101.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$) y una matriz de $R \times C$ enteros que representa un tablero de Buscaminas. Las celdas con valor `-1` contienen una mina, mientras que las celdas con `0` representan celdas vacías.
* **Objetivo:** Para cada celda vacía (`0`), calcula cuántas minas (`-1`) hay en sus 8 vecinos e incrementa el valor de la celda con dicho conteo. Conserva las celdas con mina en `-1`.
* **Salida esperada:**
  ```text
  TABLERO=
  <fila_0_del_tablero_resuelto>
  ...
  ```

### Reto 102: Rotación de Matriz 90 Grados Antihorario In-Place
* **Archivo de plantilla:** `plantillas/reto_102.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 50$) y una matriz cuadrada de $N \times N$. Rota la matriz 90 grados a la izquierda (sentido antihorario) in-place (con espacio auxiliar $O(1)$).
* **Pista:** Transpone la matriz y luego invierte el orden verticalmente de cada una de las columnas (o viceversa).
* **Salida esperada:**
  ```text
  ROTADA=
  <fila_0_rotada>
  ...
  ```

### Reto 103: Rellenar Matriz en Serpiente
* **Archivo de plantilla:** `plantillas/reto_103.cpp`
* **Descripción:** Lee `R` y `C` ($1 \le R, C \le 50$). Crea una matriz de $R \times C$ y rellénala con números consecutivos del $1$ al $R \times C$ en un recorrido de "serpiente":
  * La fila 0 se llena de izquierda a derecha.
  * La fila 1 se llena de derecha a izquierda.
  * La fila 2 se llena de izquierda a derecha, y así sucesivamente.
* **Salida esperada:**
  ```text
  SERPIENTE=
  <fila_0>
  ...
  ```

### Reto 104: Rellenar Matriz en Caracol (Espiral)
* **Archivo de plantilla:** `plantillas/reto_104.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 15$). Crea una matriz de $N \times N$ y rellénala con números del $1$ al $N^2$ siguiendo un recorrido en espiral (caracol) comenzando en la esquina superior izquierda `(0,0)` y yendo hacia adentro.
* **Salida esperada:**
  ```text
  CARACOL=
  <fila_0>
  ...
  ```

### Reto 105: Validador de Tableros Sudoku 9x9
* **Archivo de plantilla:** `plantillas/reto_105.cpp`
* **Descripción:** Lee una matriz de $9 \times 9$ enteros representativos de un tablero Sudoku. Determina si el tablero es válido según las reglas estándar:
  1. Cada fila no debe tener números del 1 al 9 repetidos.
  2. Cada columna no debe tener números del 1 al 9 repetidos.
  3. Cada una de las 9 subcuadrículas internas de $3 \times 3$ no debe tener números del 1 al 9 repetidos.
* **Salida esperada:**
  ```text
  SUDOKU=<VALIDO | INVALIDO>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_101.cpp soluciones/reto_101.cpp
# Resuelve soluciones/reto_101.cpp
python3 test_dia_7.py 101 soluciones/reto_101.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_7.py all
```
