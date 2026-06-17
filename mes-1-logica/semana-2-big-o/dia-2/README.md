# Día 2: Complejidad Cuadrática ($O(N^2)$) y Comparación de Parejas

## Teoría: La Trampa de los Bucles Anidados

Cuando un algoritmo debe comparar cada elemento de un arreglo contra todos los demás, entramos en la categoría de **Complejidad Temporal Cuadrática ($O(N^2)$)**.

### ¿Cómo se produce $O(N^2)$?
El patrón clásico que genera complejidad cuadrática es un bucle anidado dentro de otro:
```cpp
for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
        // Comparación de la pareja arr[i] y arr[j]
    }
}
```
En este caso, para un arreglo de tamaño $N$, realizamos aproximadamente:
$$\frac{N \times (N - 1)}{2} \text{ comparaciones}$$

Si $N = 1,000$, esto representa unas $500,000$ operaciones. Si $N = 100,000$, la cantidad de operaciones se eleva a **5 mil millones**, lo que hará que una computadora moderna tarde varios segundos (o incluso minutos) en terminar, mientras que un algoritmo lineal $O(N)$ tardaría menos de una milésima de segundo.

Aprender a identificar y evitar los bucles anidados innecesarios es la primera regla de oro de la optimización algorítmica.

---

## Retos del Día 2

### Reto 41: Búsqueda de Duplicados (Fuerza Bruta)
* **Archivo de plantilla:** `plantillas/reto_41.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Determina si existe al menos un elemento que aparezca repetido en el arreglo.
* **Complejidad:** Resuélvelo comparando parejas usando un bucle anidado ($O(N^2)$ en tiempo, $O(1)$ en espacio).
* **Salida esperada:**
  ```text
  DUPLICADOS=<SI | NO>
  ```

### Reto 42: Diferencia Máxima entre Dos Elementos
* **Archivo de plantilla:** `plantillas/reto_42.cpp`
* **Descripción:** Lee un entero `N` ($2 \le N \le 1000$) y `N` enteros. Encuentra la máxima diferencia absoluta entre cualquier pareja de elementos del arreglo (el valor absoluto de la resta entre los dos números).
* **Complejidad:** Aunque se puede resolver comparando todas las parejas en $O(N^2)$, ¡intenta pensar en una forma de resolverlo en tiempo lineal $O(N)$!
* **Salida esperada:**
  ```text
  DIFERENCIA=<valor_maximo_de_la_resta>
  ```

### Reto 43: Intersección de Arreglos No Ordenados
* **Archivo de plantilla:** `plantillas/reto_43.cpp`
* **Descripción:** Escribe un programa que:
  1. Lee el tamaño `N` ($1 \le N \le 500$) y los `N` enteros del primer arreglo.
  2. Lee el tamaño `M` ($1 \le M \le 500$) y los `M` enteros del segundo arreglo.
  3. Encuentra e imprime los elementos que están presentes en **ambos** arreglos.
* **Regla:** Imprime los elementos en el orden exacto en el que aparecen en el **primer arreglo**. Si un elemento de intersección está repetido en el primer arreglo, muéstralo solo una vez en la salida para evitar duplicados.
* **Salida esperada (elementos separados por un espacio):**
  ```text
  INTERSECCION=<e1> <e2> ...
  ```
  *(Si no hay intersección, imprimir simplemente `INTERSECCION=`)*

### Reto 44: Rotar Arreglo a la Derecha
* **Archivo de plantilla:** `plantillas/reto_44.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$), `N` enteros que componen el arreglo, y un entero de rotación `K` ($K \ge 0$). Rota el arreglo a la derecha `K` posiciones de forma cíclica.
* **Ejemplo:** Si el arreglo es `[1, 2, 3, 4, 5]` y $K = 2$, la salida debe ser `4 5 1 2 3`.
* **Pista:** Recuerda que rotar $K$ posiciones cuando $K \ge N$ es lo mismo que rotar `K % N` posiciones.
* **Salida esperada:**
  ```text
  ROTADO=<e1> <e2> ... <eN>
  ```

### Reto 45: Suma de Parejas (Suma Objetivo)
* **Archivo de plantilla:** `plantillas/reto_45.cpp`
* **Descripción:** Lee un entero `N` ($2 \le N \le 1000$), `N` enteros, y un número objetivo `S`. Determina si existen dos elementos en posiciones diferentes del arreglo cuya suma sea exactamente igual a `S`.
* **Complejidad:** Resuélvelo analizando todas las parejas posibles ($O(N^2)$ en tiempo).
* **Salida esperada:**
  ```text
  PAREJA=<SI | NO>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_41.cpp soluciones/reto_41.cpp
# Resuelve soluciones/reto_41.cpp
python3 test_dia_2.py 41 soluciones/reto_41.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_2.py all
```
