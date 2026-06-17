# Día 3: Algoritmos de Ordenamiento I - Bubble Sort (Ordenamiento Burbuja)

## Teoría: La Flotación de Valores en Arreglos

Ordenar un arreglo consiste en reorganizar sus elementos en una secuencia determinada (usualmente ascendente). 

El algoritmo **Bubble Sort (Ordenamiento Burbuja)** es el más elemental de todos. Funciona comparando pares de elementos adyacentes y cambiándolos de lugar si están en el orden incorrecto:

```text
[ 5, 1, 4, 2 ]  ->  ¿5 > 1? Sí. Intercambio.
[ 1, 5, 4, 2 ]  ->  ¿5 > 4? Sí. Intercambio.
[ 1, 4, 5, 2 ]  ->  ¿5 > 2? Sí. Intercambio.
[ 1, 4, 2, 5 ]  ->  (El 5 ya "flotó" a su posición final en la primera pasada)
```

### 1. Complejidad del Peor Caso ($O(N^2)$)
Si el arreglo está ordenado de forma totalmente invertida (descendente), cada elemento debe compararse e intercambiarse en cada paso. Esto requiere:
$$\frac{N \times (N - 1)}{2} \text{ comparaciones y desplazamientos}$$
Por ende, su complejidad temporal es **$O(N^2)$**.

### 2. Optimización por Parada Temprana ($O(N)$)
En su versión ingenua, Bubble Sort siempre realiza $N-1$ pasadas del bucle externo. Sin embargo, si en una pasada completa por el arreglo **no se realiza ningún intercambio**, significa que el arreglo ya está completamente ordenado.
Añadiendo una bandera booleana (`swapped`), podemos romper el bucle temprano. En el mejor caso (un arreglo que ya venía ordenado), el algoritmo solo realiza $1$ pasada y termina en tiempo lineal **$O(N)$**.

---

## Retos del Día 3

### Reto 81: Bubble Sort Estándar (Conteo de Intercambios)
* **Archivo de plantilla:** `plantillas/reto_81.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa el algoritmo Bubble Sort estándar para ordenar el arreglo de forma ascendente. Cuenta cuántos intercambios de elementos (`swap`) realiza el algoritmo en total.
* **Salida esperada:**
  ```text
  INTERCAMBIOS=<conteo_total>
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 82: Bubble Sort Optimizado (Conteo de Pasadas)
* **Archivo de plantilla:** `plantillas/reto_82.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa Bubble Sort optimizado usando la bandera de verificación de intercambios para detener la ejecución si el arreglo ya está ordenado. Muestra el número de pasadas completas del bucle externo que realizó el programa.
* **Salida esperada:**
  ```text
  PASADAS=<número_de_pasadas>
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 83: Bubble Sort Descendente
* **Archivo de plantilla:** `plantillas/reto_83.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa Bubble Sort para ordenar los elementos del arreglo de forma **descendente** (de mayor a menor).
* **Salida esperada:**
  ```text
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 84: Bubble Sort Bidireccional (Cocktail Shaker Sort)
* **Archivo de plantilla:** `plantillas/reto_84.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa el algoritmo **Cocktail Shaker Sort** (burbuja bidireccional), el cual va y viene en cada pasada: primero de izquierda a derecha (llevando el máximo al final) y luego de derecha a izquierda (llevando el mínimo al inicio), encogiendo los límites de búsqueda en cada iteración.
* **Salida esperada:**
  ```text
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 85: K-ésimo Elemento Menor (Burbuja Parcial)
* **Archivo de plantilla:** `plantillas/reto_85.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros, y un entero `K` ($1 \le K \le N$). Encuentra el **K-ésimo elemento más pequeño** del arreglo.
* **Optimización:** No ordenes todo el arreglo. Si solo necesitas el K-ésimo menor, puedes realizar únicamente las primeras `K` pasadas de un algoritmo de burbuja para colocar los `K` menores en sus posiciones iniciales de forma eficiente en tiempo $O(N \times K)$.
* **Salida esperada:**
  ```text
  ELEMENTO=<valor>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_81.cpp soluciones/reto_81.cpp
# Resuelve soluciones/reto_81.cpp
python3 test_dia_3.py 81 soluciones/reto_81.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_3.py all
```
