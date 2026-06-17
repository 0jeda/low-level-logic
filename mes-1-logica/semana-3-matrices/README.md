# Semana 3 – Matrices (Arreglos Bidimensionales) y Algoritmos de Ordenamiento Básicos

¡Bienvenido/a a la tercera semana de entrenamiento de **Low-Level Logic**!

Esta semana nos enfocaremos en dos áreas críticas de la manipulación de datos en memoria:
1. **Matrices (Arreglos 2D):** Cómo se organizan y representan los datos bidimensionales en la memoria lineal del computador, dominando el uso de bucles anidados y la aritmética de Row-Major order.
2. **Algoritmos de Ordenamiento Puro:** Analizaremos e implementaremos a mano los dos algoritmos de ordenamiento más intuitivos y fundamentales: **Bubble Sort** e **Insertion Sort**, evaluando su comportamiento en el mejor, promedio y peor de los casos.

---

## 📐 Conceptos Clave de la Semana

### 1. ¿Cómo se ve una Matriz 2D en Memoria?
Físicamente, la memoria RAM del computador es un vector lineal unidimensional. No existen las matrices "cuadradas" o "rectangulares" reales en hardware.
Cuando declaramos una matriz en C++ como `int matriz[3][4];` (3 filas y 4 columnas), el compilador la almacena de forma contigua usando el orden **Row-Major Order** (orden por filas). El arreglo se despliega linealmente en memoria de la siguiente forma:
```text
[ Fila 0, Col 0..3 ] [ Fila 1, Col 0..3 ] [ Fila 2, Col 0..3 ]
```
La fórmula que utiliza la CPU para calcular la dirección física de la celda en la fila `i` y columna `j` es:
$$\text{Dirección} = \text{Dirección Base} + ((i \times \text{ColumnasTotales}) + j) \times \text{sizeof(tipo)}$$

### 2. Algoritmos de Ordenamiento Básicos

* **Bubble Sort (Ordenamiento Burbuja):**
  * Mecánica: Compara repetidamente elementos adyacentes y los intercambia si están en el orden incorrecto. Los elementos más grandes "flotan" hacia el final en cada pasada.
  * Peor caso: $O(N^2)$ tiempo.
  * Mejor caso (optimizado): $O(N)$ tiempo si el arreglo ya está ordenado.
* **Insertion Sort (Ordenamiento por Inserción):**
  * Mecánica: Construye el arreglo ordenado elemento por elemento, insertando cada nuevo elemento en su posición correcta respecto a los ya ordenados (como organizar una baraja de cartas).
  * Peor caso: $O(N^2)$ tiempo (arreglo invertido).
  * Mejor caso: $O(N)$ tiempo (arreglo ya ordenado, con 0 desplazamientos).

---

## 📅 Ruta de Retos Diarios

* **[Día 1: Matrices en Memoria Contigua y Recorridos Básicos](./dia-1/README.md)** (Retos 71 a 75)
* **[Día 2: Recorridos de Diagonales, Espirales y Rotaciones](./dia-2/README.md)** (Retos 76 a 80)
* **[Día 3: Algoritmos de Ordenamiento I - Bubble Sort](./dia-3/README.md)** (Retos 81 a 85)
* **[Día 4: Algoritmos de Ordenamiento II - Insertion Sort](./dia-4/README.md)** (Retos 86 a 90)
* **[Día 5: Búsqueda y Sumas en Matrices Especiales](./dia-5/README.md)** (Retos 91 a 95)
* **[Día 6: Ordenamiento In-Place en Matrices](./dia-6/README.md)** (Retos 96 a 100)
* **[Día 7: El Gran Reto - Generación de Tableros de Buscaminas](./dia-7/README.md)** (Retos 101 a 105)

---

## 🛠️ Instrucciones de Trabajo
Entra al subdirectorio correspondiente para comenzar el día:
```bash
cd mes-1-logica/semana-3-matrices/dia-1/
cp plantillas/reto_71.cpp soluciones/reto_71.cpp
# Edita soluciones/reto_71.cpp
python3 test_dia_1.py soluciones/reto_71.cpp
```
