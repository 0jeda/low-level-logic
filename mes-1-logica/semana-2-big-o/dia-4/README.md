# Día 4: Optimización Espacial (Algoritmos In-Place $O(1)$)

## Teoría: Complejidad Espacial y el Valor del Espacio Auxiliar

Hasta ahora nos hemos concentrado en la velocidad (Complejidad Temporal). Sin embargo, en el desarrollo real de software —particularmente en sistemas embebidos, móviles o servidores de alto tráfico— la **Complejidad Espacial** (el consumo de memoria RAM) es igual de importante.

### ¿Qué es la memoria auxiliar $O(1)$?
Un algoritmo trabaja **in-place** (en su propio lugar) si modifica la estructura de datos original directamente sobre las mismas celdas de memoria que le fueron entregadas, sin realizar copias ni reservar memoria dinámica proporcional al tamaño de los datos ($N$).
* Un algoritmo que duplica el arreglo en memoria auxiliar tiene una complejidad espacial de **$O(N)$**.
* Un algoritmo que solo usa un par de variables simples para el control del bucle y los intercambios tiene una complejidad espacial de **$O(1)$** (memoria auxiliar constante).

Optimizar el espacio requiere un control muy fino de los índices y punteros de lectura y escritura.

---

## Retos del Día 4

### Reto 51: Eliminar Duplicados de un Arreglo Ordenado In-Place
* **Archivo de plantilla:** `plantillas/reto_51.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros ordenados de forma ascendente. Modifica el arreglo directamente para eliminar todos los elementos duplicados, compactando los elementos únicos al inicio.
* **Complejidad:** Debe completarse en $O(N)$ en tiempo y $O(1)$ en espacio auxiliar utilizando dos punteros (uno de lectura y uno de escritura lenta). Tu programa debe retornar la nueva longitud lógica `K` del arreglo e imprimir únicamente los `K` elementos únicos.
* **Salida esperada:**
  ```text
  ARREGLO=<u1> <u2> ... <uK>
  ```

### Reto 52: Mover Ceros al Final
* **Archivo de plantilla:** `plantillas/reto_52.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Mueve todos los elementos que sean `0` al final del arreglo, pero **manteniendo el orden relativo** del resto de los elementos distintos de cero.
* **Complejidad:** Debe hacerse in-place ($O(1)$ en espacio) y en un solo recorrido lineal ($O(N)$ en tiempo).
* **Salida esperada:**
  ```text
  ARREGLO=<e1> <e2> ... <eN>
  ```

### Reto 53: Combinar Dos Arreglos Ordenados (Merge)
* **Archivo de plantilla:** `plantillas/reto_53.cpp`
* **Descripción:** Escribe un programa que:
  1. Lee el tamaño `N` ($1 \le N \le 500$) y `N` enteros ordenados del primer arreglo.
  2. Lee el tamaño `M` ($1 \le M \le 500$) y `M` enteros ordenados del segundo arreglo.
  3. Combina ambos en un único arreglo de tamaño $N + M$ que se mantenga ordenado ascendentemente.
* **Complejidad:** No unas los arreglos y luego los ordenes (eso sería ineficiente). Debes combinarlos en tiempo lineal **$O(N + M)$** usando un puntero de lectura independiente para cada arreglo.
* **Salida esperada:**
  ```text
  COMBINADO=<e1> <e2> ... <e_N+M>
  ```

### Reto 54: Rotar Arreglo In-Place (Sin Memoria Auxiliar)
* **Archivo de plantilla:** `plantillas/reto_54.cpp`
* **Descripción:** Resuelve el reto de rotación del Día 2 (Reto 44) pero con una restricción extrema: **está prohibido declarar arreglos auxiliares**. Debes rotar el arreglo directamente en su propio bloque de memoria.
* **Pista (El truco de la triple inversión):** 
  1. Asegura $K = K \mathbin{\%} N$.
  2. Invierte todo el arreglo completo.
  3. Invierte los primeros $K$ elementos.
  4. Invierte los restantes $N - K$ elementos.
* **Complejidad:** $O(N)$ en tiempo y $O(1)$ en espacio auxiliar.
* **Salida esperada:**
  ```text
  ROTADO=<e1> <e2> ... <eN>
  ```

### Reto 55: Algoritmo de Votación de Boyer-Moore
* **Archivo de plantilla:** `plantillas/reto_55.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Encuentra el **elemento mayoritario** (aquel elemento que aparece estrictamente más de $N / 2$ veces en el arreglo). Se garantiza que este elemento siempre existe.
* **Complejidad:** Resuélvelo en $O(N)$ en tiempo y $O(1)$ en espacio de memoria auxiliar implementando el Algoritmo de Votación de Boyer-Moore.
* **Salida esperada:**
  ```text
  MAYORITARIO=<valor>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_51.cpp soluciones/reto_51.cpp
# Resuelve soluciones/reto_51.cpp
python3 test_dia_4.py 51 soluciones/reto_51.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_4.py all
```
