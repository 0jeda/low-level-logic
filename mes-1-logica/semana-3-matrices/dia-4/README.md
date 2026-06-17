# Día 4: Algoritmos de Ordenamiento II - Insertion Sort (Ordenamiento por Inserción)

## Teoría: La Inserción Ordenada (Baraja de Cartas)

El algoritmo **Insertion Sort (Ordenamiento por Inserción)** imita la forma en que los seres humanos organizamos una mano de cartas de juego.
Mantiene una división imaginaria en el arreglo: a la izquierda la parte ya ordenada, y a la derecha los elementos pendientes. 

En cada paso, el algoritmo toma el primer elemento de la parte desordenada (llamado `key` o clave) y lo compara hacia atrás con los elementos ordenados, desplazándolos una posición a la derecha hasta encontrar el lugar correcto donde "insertar" el `key`.

```text
Arreglo: [ 2, 8, 5, 3 ]   -> Fila ordenada inicial: [2]. Clave = 8.
¿2 > 8? No. Queda igual: [2, 8, 5, 3].
Siguiente clave = 5.
¿8 > 5? Sí. Desplazamos el 8: [2, 8, 8, 3].
¿2 > 5? No. Insertamos el 5 en la posición libre: [2, 5, 8, 3].
Siguiente clave = 3.
¿8 > 3? Sí. Desplazamos: [2, 5, 8, 8].
¿5 > 3? Sí. Desplazamos: [2, 5, 5, 8].
¿2 > 3? No. Insertamos: [2, 3, 5, 8]. ¡Terminado!
```

### 1. Complejidad y Ventajas
* **Peor caso ($O(N^2)$):** Si el arreglo está ordenado de forma inversa, cada inserción requiere desplazar todos los elementos de la izquierda.
* **Mejor caso ($O(N)$):** Si el arreglo ya está ordenado, el bucle de inserción realiza exactamente 0 desplazamientos. Esto lo hace el algoritmo preferido para arreglos que ya están "casi ordenados".

---

## Retos del Día 4

### Reto 86: Insertion Sort Estándar (Conteo de Desplazamientos)
* **Archivo de plantilla:** `plantillas/reto_86.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa el algoritmo Insertion Sort estándar de forma ascendente. Cuenta cuántos desplazamientos individuales de celdas realiza el algoritmo en total.
* **Salida esperada:**
  ```text
  DESPLAZAMIENTOS=<conteo>
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 87: Insertion Sort Descendente
* **Archivo de plantilla:** `plantillas/reto_87.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa Insertion Sort para ordenar los elementos del arreglo de forma **descendente** (de mayor a menor).
* **Salida esperada:**
  ```text
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 88: Inserción de un Elemento Desalineado
* **Archivo de plantilla:** `plantillas/reto_88.cpp`
* **Descripción:** Lee un entero `N` ($2 \le N \le 1000$) y `N` enteros. Se garantiza que los primeros $N-1$ elementos del arreglo ya están ordenados ascendentemente, y que solo el último elemento (en el índice $N-1$) está fuera de lugar.
* **Objetivo:** Realiza un único paso del bucle interno de inserción para colocar este último elemento en su posición correcta en tiempo lineal **$O(N)$**.
* **Salida esperada:**
  ```text
  ORDENADO=<e1> <e2> ... <eN>
  ```

### Reto 89: Ordenamiento de Cadena de Caracteres
* **Archivo de plantilla:** `plantillas/reto_89.cpp`
* **Descripción:** Lee una palabra de letras minúsculas (longitud $N \le 100$). Ordena los caracteres de la palabra alfabéticamente usando Insertion Sort y muestra la palabra resultante.
* **Salida esperada:**
  ```text
  ORDENADO=<palabra_ordenada>
  ```

### Reto 90: Ordenamiento por Inserción Binaria (Binary Insertion Sort)
* **Archivo de plantilla:** `plantillas/reto_90.cpp`
* **Descripción:** Lee un entero `N` ($1 \le N \le 1000$) y `N` enteros. Implementa el algoritmo **Binary Insertion Sort**.
* **Pista:** En lugar de buscar linealmente hacia atrás la posición correcta de inserción para `arr[i]`, utiliza **Búsqueda Binaria** sobre la parte ya ordenada `arr[0...i-1]` para encontrar la posición exacta en tiempo $O(\log i)$. Luego, desplaza los elementos necesarios a la derecha e inserta el elemento.
* **Salida esperada:**
  ```text
  ORDENADO=<e1> <e2> ... <eN>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_86.cpp soluciones/reto_86.cpp
# Resuelve soluciones/reto_86.cpp
python3 test_dia_4.py 86 soluciones/reto_86.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_4.py all
```
