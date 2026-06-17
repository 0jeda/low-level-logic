# Día 6: Complejidad Espacial y Arreglos de Frecuencia

## Teoría: Mapeo Directo e Indexación por Frecuencias

Muchas veces necesitamos contar cuántas veces aparece un elemento en un conjunto de datos (calcular su frecuencia). 

La solución obvia es recorrer el arreglo para cada elemento buscando coincidencias, lo que toma tiempo cuadrático $O(N^2)$. Sin embargo, si el rango de valores posibles es acotado (por ejemplo, números del 0 al 9, o letras del alfabeto), podemos usar una técnica de bajo nivel llamada **Mapeo Directo o Arreglo de Frecuencias**.

### ¿Cómo funciona un Arreglo de Frecuencias?
Consiste en declarar un arreglo auxiliar inicializado en ceros, donde **el índice del arreglo representa el valor que queremos contar**.

* Si leemos la letra `'c'` (cuyo índice relativo en el alfabeto es 2, ya que `'c' - 'a' = 2`), hacemos:
  `frecuencia[2]++;`
* Al terminar un único recorrido lineal de los datos, el arreglo de frecuencias tiene el conteo exacto de todas las apariciones en tiempo **$O(N)$**.
* La complejidad espacial es **$O(K)$**, donde $K$ es el rango de valores posibles (un tamaño pequeño y constante como 26 para el alfabeto o 10 para dígitos).

---

## Retos del Día 6

### Reto 61: Conteo de Frecuencias en Rango $[0, 9]$
* **Archivo de plantilla:** `plantillas/reto_61.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Todos los elementos están garantizados de estar en el rango de un solo dígito decimal ($0$ a $9$). Cuenta la frecuencia de cada número y muéstralos en orden ascendente (omitiendo los que tengan frecuencia 0).
* **Complejidad:** Debe resolverse en $O(N)$ en tiempo usando un arreglo de frecuencias de tamaño 10.
* **Salida esperada (un número por línea):**
  ```text
  <número>:<frecuencia>
  ```

### Reto 62: El Elemento Único en Parejas (El truco de XOR)
* **Archivo de plantilla:** `plantillas/reto_62.cpp`
* **Descripción:** Lee un entero impar `N` ($1 \le N \le 999$) y `N` enteros. En este arreglo, todos los elementos aparecen exactamente dos veces, excepto uno de ellos que aparece solo una vez. Encuentra ese elemento.
* **Complejidad:** Debe resolverse en $O(N)$ en tiempo y $O(1)$ en espacio de memoria auxiliar.
* **Pista:** El operador XOR (`^`) es asociativo, conmutativo, y tiene la propiedad de que `X ^ X = 0` y `0 ^ Y = Y`. Si aplicas XOR a todos los elementos del arreglo consecutivamente, las parejas se cancelarán entre sí y solo sobrevivirá el elemento único.
* **Salida esperada:**
  ```text
  UNICO=<valor>
  ```

### Reto 63: Encontrar el Número Faltante
* **Archivo de plantilla:** `plantillas/reto_63.cpp`
* **Descripción:** Lee un entero `N` ($2 \le N \le 1000$). El arreglo que sigue tiene tamaño $N-1$ y contiene $N-1$ enteros distintos en el rango del $1$ al $N$. Esto significa que falta exactamente un número. Encuéntralo.
* **Complejidad:** $O(N)$ en tiempo y $O(1)$ en espacio auxiliar (sin usar arreglos adicionales).
* **Pista:** Calcula la suma teórica de todos los números del $1$ al $N$ usando la fórmula de Gauss: $S = \frac{N(N+1)}{2}$. Réstale la suma de los elementos reales del arreglo. La diferencia es el número faltante.
* **Salida esperada:**
  ```text
  FALTANTE=<valor>
  ```

### Reto 64: Detector de Anagramas
* **Archivo de plantilla:** `plantillas/reto_64.cpp`
* **Descripción:** Lee dos palabras compuestas por letras minúsculas (sin espacios, longitud máxima de 100). Determina si las dos palabras son anagramas (si tienen exactamente las mismas letras con las mismas frecuencias, como "roma" y "amor").
* **Complejidad:** $O(N)$ en tiempo y $O(1)$ en espacio auxiliar usando un arreglo de frecuencia de tamaño 26.
* **Salida esperada:**
  ```text
  ANAGRAMA=<SI | NO>
  ```

### Reto 65: Conteo de Elementos Únicos con Offset
* **Archivo de plantilla:** `plantillas/reto_65.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros que pueden ser positivos o negativos en el rango acotado de $[-1000, 1000]$. Cuenta cuántos elementos **únicos** (diferentes) existen en el arreglo.
* **Pista:** Como el rango incluye números negativos, no puedes usar directamente el valor del número como índice en el arreglo de frecuencias. Debes aplicar un **desplazamiento (offset)** sumándole `1000` a cada número para mapear el rango $[-1000, 1000]$ a los índices de memoria $[0, 2000]$.
* **Salida esperada:**
  ```text
  UNICOS=<cantidad_elementos_unicos>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_61.cpp soluciones/reto_61.cpp
# Resuelve soluciones/reto_61.cpp
python3 test_dia_6.py 61 soluciones/reto_61.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_6.py all
```
