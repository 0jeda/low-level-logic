# Día 7: El Gran Reto de Complejidad y Git Avanzado

## Teoría: Optimización Extrema y la Explicación del Código

Hoy completamos la segunda semana de entrenamiento. A estas alturas, ya has aprendido a:
1. Acceder y recorrer arreglos en tiempo lineal $O(N)$.
2. Identificar el impacto de los bucles anidados $O(N^2)$.
3. Reducir drásticamente la búsqueda de elementos usando Búsqueda Binaria $O(\log N)$.
4. Modificar datos de forma contigua con espacio auxiliar $O(1)$ (In-place).

El último paso para ser un programador profesional es **saber comunicar tus decisiones de diseño**. Cuando crees tu Pull Request (PR) en GitHub para integrar la Semana 2, deberás documentar y justificar detalladamente en la descripción del PR por qué tus algoritmos cumplen con las restricciones de complejidad temporal y espacial requeridas.

---

## Retos del Día 7

### Reto 66: Búsqueda Binaria en un Arreglo Rotado
* **Archivo de plantilla:** `plantillas/reto_66.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros, y un valor objetivo `T`. El arreglo original estaba ordenado ascendentemente, pero luego fue rotado cíclicamente un número desconocido de posiciones (por ejemplo, `[4, 5, 6, 7, 0, 1, 2]`). Encuentra el índice de `T`.
* **Complejidad:** Debe resolverse en tiempo **$O(\log N)$** (Búsqueda Binaria adaptada).
* **Pista:** En cualquier punto de la división binaria, al menos una de las dos mitades (izquierda o derecha) está garantizada de estar ordenada. Determina cuál mitad está ordenada y verifica si `T` cae dentro de sus límites; de lo contrario, busca en la otra mitad.
* **Salida esperada:**
  ```text
  INDICE=<índice_encontrado_o_-1>
  ```

### Reto 67: Encontrar el Elemento Más Cercano
* **Archivo de plantilla:** `plantillas/reto_67.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros ordenados ascendentemente, y un valor objetivo `T`. Encuentra el elemento del arreglo cuyo valor numérico sea el más cercano a `T` (es decir, que minimice la distancia $|arr[i] - T|$). Si hay un empate, devuelve el elemento de menor valor.
* **Complejidad:** Debe resolverse en tiempo **$O(\log N)$**.
* **Salida esperada:**
  ```text
  CERCANO=<valor_del_elemento>
  ```

### Reto 68: Intersección de Arreglos Ordenados (Dos Punteros)
* **Archivo de plantilla:** `plantillas/reto_68.cpp`
* **Descripción:** Lee el tamaño `N` ($1 \le N \le 1000$) y `N` enteros ordenados de un primer arreglo. Luego lee el tamaño `M` ($1 \le M \le 1000$) y `M` enteros ordenados de un segundo arreglo. Encuentra la intersección de ambos.
* **Complejidad:** Resuélvelo en tiempo lineal **$O(N + M)$** y espacio auxiliar **$O(1)$** usando la técnica de dos punteros (uno para cada arreglo, avanzando el que apunte al número menor). Evita imprimir duplicados si se repiten elementos.
* **Salida esperada:**
  ```text
  INTERSECCION=<e1> <e2> ...
  ```

### Reto 69: Suma de Tres Elementos (3-Sum)
* **Archivo de plantilla:** `plantillas/reto_69.cpp`
* **Descripción:** Lee un entero `N` ($3 \le N \le 200$), `N` enteros desordenados, y una suma objetivo `T`. Determina si existen tres elementos en posiciones distintas del arreglo cuya suma sea exactamente igual a `T`.
* **Complejidad:** Puedes ordenar el arreglo primero (en $O(N^2)$ usando Bubble Sort) y luego resolverlo en **$O(N^2)$** en tiempo usando la técnica de dos punteros sobre los extremos para buscar la pareja que complete el tercer elemento.
* **Salida esperada:**
  ```text
  PAREJA3=<SI | NO>
  ```

### Reto 70: Peor Caso de la Búsqueda Binaria
* **Archivo de plantilla:** `plantillas/reto_70.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 2 \times 10^9$) que representa el tamaño de un arreglo ordenado conceptual. Calcula e imprime el número máximo de comparaciones (operaciones de división a la mitad) que la búsqueda binaria realizaría en el peor de los casos para determinar si un elemento existe.
* **Complejidad:** $O(\log N)$ en tiempo.
* **Obligación en PR:** En el texto descriptivo de tu Pull Request de esta semana, debes explicar la deducción matemática de la fórmula que utilizaste.
* **Salida esperada:**
  ```text
  COMPARACIONES=<cantidad>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_66.cpp soluciones/reto_66.cpp
# Resuelve soluciones/reto_66.cpp
python3 test_dia_7.py 66 soluciones/reto_66.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_7.py all
```
