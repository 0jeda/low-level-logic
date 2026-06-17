# Día 5: Ventanas Deslizantes (Sliding Window) y Subarreglos

## Teoría: Optimizar Bucles Anidados sobre Ventanas

Un subarreglo es una secuencia continua de elementos dentro de un arreglo. Muchos problemas requieren calcular propiedades (como sumas, promedios o máximos) de todos los subarreglos posibles.

### 1. La Técnica de Ventana Deslizante (Sliding Window)
Si queremos calcular la suma de cada subarreglo de tamaño fijo $K$, la solución de fuerza bruta vuelve a calcular la suma desde cero para cada posición, tomando tiempo $O(N \times K)$.

La **Ventana Deslizante** optimiza esto al notar que la ventana al moverse un paso a la derecha pierde el elemento más a la izquierda y gana uno nuevo a la derecha. Podemos calcular la nueva suma en tiempo constante **$O(1)$**:
$$\text{Suma Nueva} = \text{Suma Anterior} - \text{arr[izq]} + \text{arr[der]}$$
Esto reduce la complejidad de la búsqueda a **$O(N)$** total.

### 2. Arreglos de Suma Acumulada (Prefix Sum)
Para responder rápidamente a la pregunta "¿cuánto suman los elementos del índice $L$ al $R$?", podemos precalcular un arreglo `prefijo` donde cada posición almacena la suma de todos los elementos anteriores:
$$\text{prefijo}[i] = \text{arr}[0] + \text{arr}[1] + ... + \text{arr}[i]$$
Una vez calculado en $O(N)$, cualquier consulta de suma en rango se responde en **$O(1)$**:
$$\text{Suma}(L, R) = \text{prefijo}[R] - \text{prefijo}[L-1]$$

---

## Retos del Día 5

### Reto 56: Suma Máxima de Subarreglo de Tamaño Fijo K
* **Archivo de plantilla:** `plantillas/reto_56.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros y el tamaño de ventana `K` ($1 \le K \le N$). Encuentra la suma máxima que se puede obtener a partir de cualquier subarreglo contiguo de tamaño `K`.
* **Complejidad:** Debe resolverse en $O(N)$ en tiempo usando Ventana Deslizante.
* **Salida esperada:**
  ```text
  MAX_SUMA=<valor>
  ```

### Reto 57: Subarreglo Más Corto con Suma Objetivo
* **Archivo de plantilla:** `plantillas/reto_57.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros **estrictamente positivos**, y un valor objetivo `S`. Encuentra la **longitud mínima** de un subarreglo contiguo cuya suma sea mayor o igual a `S`. Si ningún subarreglo cumple la condición, imprime `0`.
* **Complejidad:** Debe resolverse en $O(N)$ en tiempo usando dos punteros de ventana variable.
* **Salida esperada:**
  ```text
  MIN_LONGITUD=<valor>
  ```

### Reto 58: Consultas Rápidas de Suma en Rango (Prefix Sum)
* **Archivo de plantilla:** `plantillas/reto_58.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros, y un número de consultas `Q` ($1 \le Q \le 100$). A continuación lee `Q` parejas de índices `L` y `R` ($0 \le L \le R < N$).
* **Complejidad:** Calcula un arreglo de sumas acumuladas (Prefix Sum) en $O(N)$ para responder cada una de las `Q` consultas en tiempo constante $O(1)$.
* **Salida esperada (una línea por cada consulta):**
  ```text
  SUMA=<resultado_consulta>
  ```

### Reto 59: Detector de Subarreglo con Suma Cero
* **Archivo de plantilla:** `plantillas/reto_59.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 100$) y `N` enteros (que pueden ser positivos, negativos o cero). Determina si existe algún subarreglo contiguo cuya suma de elementos sea exactamente `0`.
* **Salida esperada:**
  ```text
  SUMA_CERO=<SI | NO>
  ```

### Reto 60: Algoritmo de Kadane (Suma Máxima)
* **Archivo de plantilla:** `plantillas/reto_60.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros que representan un arreglo con valores positivos y negativos. Encuentra la **suma máxima** de cualquier subarreglo continuo usando el Algoritmo de Kadane.
* **Complejidad:** $O(N)$ en tiempo y $O(1)$ en espacio de memoria auxiliar.
* **Salida esperada:**
  ```text
  MAX_KADANE=<valor>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_56.cpp soluciones/reto_56.cpp
# Resuelve soluciones/reto_56.cpp
python3 test_dia_5.py 56 soluciones/reto_56.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_5.py all
```
