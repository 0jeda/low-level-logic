# Día 3: Paso de Arreglos 1D a Funciones

## Teoría: Decaimiento de Arreglos (Array Decay) a Punteros

En C++, cuando declaramos una función que toma un arreglo lineal como argumento:

```cpp
void imprimir(int arr[], int tam);
```

...el compilador **no copia** el contenido del arreglo en un nuevo Stack Frame. Por razones de rendimiento histórico y de diseño del lenguaje C, el parámetro `arr[]` decae implícitamente a un **puntero al primer elemento** del arreglo (`int* arr`).

### Consecuencias Clave:
1. **Pérdida de tamaño (`sizeof`):** Dentro de la función, hacer `sizeof(arr)` no devolverá el tamaño total en bytes del arreglo, sino el tamaño de un puntero (usualmente 8 bytes en sistemas de 64 bits). Por ello, **siempre debemos pasar un parámetro adicional** que indique el tamaño del arreglo (`tam` o `size`).
2. **Modificación implícita por referencia:** Cualquier modificación a los elementos `arr[i]` dentro de la función alterará directamente el arreglo original declarado en `main` u otra función llamadora.
3. **Punteros equivalentes:** Las siguientes firmas son exactamente equivalentes para el compilador:
   * `void func(int arr[], int tam)`
   * `void func(int* arr, int tam)`

---

## Retos del Día 3

### Reto 116: Sumador de Arreglo
* **Archivo de plantilla:** `plantillas/reto_116.cpp`
* **Descripción:** Lee un entero `N` y luego `N` enteros. Implementa la función `int sumarArreglo(const int arr[], int tam)` que recorra el arreglo y retorne la suma de todos sus elementos.
* **Salida esperada:**
  ```text
  SUMA=<suma_total>
  ```

### Reto 117: Escalar de Arreglo
* **Archivo de plantilla:** `plantillas/reto_117.cpp`
* **Descripción:** Lee `N` enteros, y finalmente un número `factor`. Implementa la función `void escalarArreglo(int arr[], int tam, int factor)` que multiplique cada elemento del arreglo original por dicho `factor`.
* **Salida esperada:**
  ```text
  ARR=[x1,x2,...,xn]
  ```

### Reto 118: Duplicador y Copia de Seguridad
* **Archivo de plantilla:** `plantillas/reto_118.cpp`
* **Descripción:** Lee `N` enteros. Implementa `void copiarArreglo(const int origen[], int destino[], int tam)` que copie exactamente los elementos de `origen` a `destino`. Imprime el arreglo de destino para comprobar el correcto funcionamiento de la copia.
* **Salida esperada:**
  ```text
  DESTINO=[x1,x2,...,xn]
  ```

### Reto 119: Búsqueda Lineal Modular
* **Archivo de plantilla:** `plantillas/reto_119.cpp`
* **Descripción:** Lee `N` enteros, y luego un entero `buscado`. Implementa `int buscarElemento(const int arr[], int tam, int buscado)` que retorne el índice (0-indexado) de la primera aparición de `buscado` o `-1` si no se encuentra.
* **Salida esperada:**
  ```text
  INDICE=<indice>
  ```

### Reto 120: Inversión In-Place (En Sitio)
* **Archivo de plantilla:** `plantillas/reto_120.cpp`
* **Descripción:** Lee `N` enteros. Implementa `void invertirArreglo(int arr[], int tam)` que invierta los elementos del arreglo modificándolo directamente en su dirección de memoria original, usando un único arreglo y un bucle que realice swaps.
* **Salida esperada:**
  ```text
  INVERTIDO=[x1,x2,...,xn]
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_116.cpp soluciones/reto_116.cpp
# Resuelve soluciones/reto_116.cpp
python3 test_dia_3.py soluciones/reto_116.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_3.py all
```
