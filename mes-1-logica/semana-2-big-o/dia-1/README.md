# Día 1: Arreglos Estáticos y Acceso Lineal

## Teoría: La Fisiología del Arreglo en Memoria

Un **arreglo (array)** es la estructura de datos más básica de la informática. Se define como una colección de elementos del mismo tipo almacenados de forma contigua en memoria.

### Aritmética de Punteros y Dirección Base
Cuando declaras un arreglo como `int arr[5];`, el compilador reserva un bloque de 20 bytes contiguos en la memoria (5 enteros × 4 bytes cada uno). El nombre del arreglo (`arr`) en C++ actúa como un puntero constante que apunta a la **Dirección Base** (la celda de memoria del primer elemento, `arr[0]`).

Para acceder a `arr[i]`, el computador calcula la dirección física del elemento mediante una multiplicación constante:
$$\text{Dirección Física} = \text{Dirección Base} + (i \times \text{sizeof(tipo)})$$

Este cálculo aritmético directo tarda exactamente el mismo tiempo sin importar si el índice `i` es 0 o 100,000. Por eso decimos que el acceso por índice en un arreglo es de **Complejidad Temporal $O(1)$** (tiempo constante).

---

## Retos del Día 1

### Reto 36: Simulación de Aritmética de Direcciones
* **Archivo de plantilla:** `plantillas/reto_36.cpp`
* **Descripción:** Lee un entero `N` (tamaño del arreglo, $1 \le N \le 100$), seguido de `N` enteros que componen el arreglo. Finalmente, lee un índice `i`.
* **Objetivo:** Simula el cálculo del offset en bytes que realiza la CPU para acceder al elemento en la posición `i`, considerando que cada entero (`int`) ocupa exactamente **4 bytes** en memoria. Si el índice `i` está fuera de los límites del arreglo ($i < 0$ o $i \ge N$), muestra un error.
* **Salida esperada:**
  - Si el índice es válido:
    ```text
    VALOR=<valor_en_indice_i>
    OFFSET=<desplazamiento_en_bytes_desde_el_inicio>
    ```
  - Si es inválido: `ERROR`

### Reto 37: Máximo y Mínimo en un Solo Recorrido
* **Archivo de plantilla:** `plantillas/reto_37.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Encuentra el elemento máximo y el mínimo del arreglo en un único bucle ($O(N)$ en tiempo y $O(1)$ en espacio auxiliar).
* **Restricción:** No utilices algoritmos de ordenamiento ni ordenes el arreglo. Debes hacer la comparación a mano en una sola pasada.
* **Salida esperada:**
  ```text
  MAX=<valor_maximo>
  MIN=<valor_minimo>
  ```

### Reto 38: Suma y Promedio Seguro
* **Archivo de plantilla:** `plantillas/reto_38.cpp`
* **Descripción:** Lee un entero `N` ($0 \le N \le 1000$) y `N` enteros. Calcula la suma de todos los elementos y su promedio.
* **Regla especial:** Si `N = 0`, el arreglo está vacío; en ese caso muestra `SUMA=0` y `PROMEDIO=0`. Asegura que el promedio se imprima con decimales exactos.
* **Salida esperada:**
  ```text
  SUMA=<suma_total>
  PROMEDIO=<promedio_con_decimales>
  ```

### Reto 39: Inversión de Arreglo In-Place ($O(1)$ en Espacio)
* **Archivo de plantilla:** `plantillas/reto_39.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Invierte el orden de los elementos del arreglo directamente sobre la misma memoria (sin declarar un segundo arreglo auxiliar).
* **Complejidad:** Debe completarse en $O(N)$ en tiempo (recorriendo hasta la mitad del arreglo) y $O(1)$ en espacio de memoria auxiliar.
* **Salida esperada (elementos separados por un espacio):**
  ```text
  ARREGLO=<e1> <e2> ... <eN>
  ```

### Reto 40: Detector de Orden Ascendente
* **Archivo de plantilla:** `plantillas/reto_40.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Determina si el arreglo está ordenado de forma ascendente (es decir, cada elemento es menor o igual al que le sigue).
* **Complejidad:** $O(N)$ en tiempo.
* **Salida esperada:**
  ```text
  ORDENADO=<SI | NO>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_36.cpp soluciones/reto_36.cpp
# Resuelve soluciones/reto_36.cpp
python3 test_dia_1.py 36 soluciones/reto_36.cpp
```
O prueba todos los retos resueltos del Día 1:
```bash
python3 test_dia_1.py all
```
