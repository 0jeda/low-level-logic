# Día 3: Búsqueda Lineal vs. Búsqueda Binaria ($O(\log N)$)

## Teoría: El Poder del Crecimiento Logarítmico

Buscar información es una de las tareas más comunes de la informática. Dependiendo de si los datos están organizados (ordenados) o no, tenemos dos estrategias muy diferentes:

### 1. Búsqueda Lineal ($O(N)$)
Si el arreglo está desordenado, no hay atajos: debemos inspeccionar cada elemento uno por uno, de izquierda a derecha.
* **Peor caso:** El elemento está al final del arreglo o no existe. Hacemos $N$ comparaciones.
* **Complejidad:** $O(N)$ en tiempo.

### 2. Búsqueda Binaria ($O(\log N)$)
Si el arreglo **ya está ordenado**, podemos usar la estrategia de "Divide y Vencerás". 
1. Miramos el elemento central.
2. Si es el objetivo, terminamos.
3. Si el objetivo es menor, sabemos que debe estar en la mitad izquierda. Descartamos por completo la mitad derecha.
4. Si el objetivo es mayor, descartamos la mitad izquierda.
5. Repetimos el proceso con la mitad restante.

Como el espacio de búsqueda se reduce a la mitad en cada paso, el número máximo de preguntas para un arreglo de tamaño $N$ es $\log_2 N$.

| Tamaño del Arreglo ($N$) | Pasos Máximos con Búsqueda Lineal | Pasos Máximos con Búsqueda Binaria |
| :--- | :--- | :--- |
| $10$ | $10$ | $4$ |
| $1,000$ | $1,000$ | $10$ |
| $1,000,000$ | $1,000,000$ | $20$ |
| $4,000,000,000$ | $4,000,000,000$ | $32$ |

¡La diferencia es abismal! Pasar de 4 mil millones de operaciones a solo 32 es la diferencia entre esperar horas o recibir la respuesta de inmediato.

---

## Retos del Día 3

### Reto 46: Búsqueda Lineal Estándar
* **Archivo de plantilla:** `plantillas/reto_46.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros desordenados, y un valor objetivo `T`. Busca `T` en el arreglo de izquierda a derecha y devuelve el índice de su **primera aparición**. Si no existe, devuelve `-1`.
* **Salida esperada:**
  ```text
  INDICE=<índice_encontrado>
  ```

### Reto 47: Búsqueda Binaria Iterativa
* **Archivo de plantilla:** `plantillas/reto_47.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros **garantizados de estar ordenados de forma ascendente**, y un valor objetivo `T`. Implementa la Búsqueda Binaria de forma iterativa (usando un bucle y dos punteros/índices `izq` y `der`) para encontrar `T`. Si existe, devuelve su índice; si no, devuelve `-1`.
* **Complejidad:** Debe ser estrictamente $O(\log N)$ en tiempo.
* **Salida esperada:**
  ```text
  INDICE=<índice_encontrado>
  ```

### Reto 48: Primera Ocurrencia de un Duplicado
* **Archivo de plantilla:** `plantillas/reto_48.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros ordenados (que pueden tener valores duplicados), y un objetivo `T`. Encuentra el **primer índice (el más a la izquierda)** donde aparece `T` usando Búsqueda Binaria modificada.
* **Pista:** Cuando el algoritmo encuentre que el elemento medio es igual a `T`, no debe detenerse inmediatamente. Debe registrar esa posición como posible respuesta y continuar buscando en el subarreglo izquierdo (`der = medio - 1`).
* **Salida esperada:**
  ```text
  INDICE=<primer_indice_de_T>
  ```

### Reto 49: Punto de Inserción Correcto (`lower_bound`)
* **Archivo de plantilla:** `plantillas/reto_49.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros ordenados ascendentemente, y un valor `T`. Determina el índice de la posición donde debería insertarse `T` para que el arreglo siga estando ordenado. Si `T` ya existe en el arreglo, devuelve el primer índice donde aparece.
* **Complejidad:** Debe resolverse en $O(\log N)$ en tiempo.
* **Salida esperada:**
  ```text
  INDICE=<posicion_de_insercion>
  ```

### Reto 50: Raíz Cuadrada Entera por Búsqueda Binaria
* **Archivo de plantilla:** `plantillas/reto_50.cpp`
* **Descripción:** Lee un entero positivo `X` ($0 \le X \le 10^{12}$) que cabe en un `long long`. Encuentra la **raíz cuadrada entera** de `X` (el mayor entero `y` tal que $y^2 \le X$).
* **Restricción:** Está prohibido usar `<cmath>`, `std::sqrt()` y aritmética de flotantes. Debes resolverlo realizando búsqueda binaria en el rango de números enteros $[0, X]$.
* **Pista:** El rango de búsqueda binaria se define sobre valores lógicos, no sobre memoria física. Ten cuidado con los desbordamientos al calcular `medio * medio` (usa tipos `long long`).
* **Salida esperada:**
  ```text
  RAIZ=<valor_entero>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_46.cpp soluciones/reto_46.cpp
# Resuelve soluciones/reto_46.cpp
python3 test_dia_3.py 46 soluciones/reto_46.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_3.py all
```
