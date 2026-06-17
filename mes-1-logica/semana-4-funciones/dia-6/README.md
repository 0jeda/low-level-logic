# Día 6: Aritmética de Punteros y la Relación con los Arreglos

## Teoría: La Memoria como una Gran Cuadrícula Direccionable

Un **puntero** es una variable que almacena una **dirección de memoria** en lugar de un valor de datos común. 

### Operadores Fundamentales:
* **Operador de dirección (`&`):** Obtiene la dirección de memoria física de una variable.
* **Operador de desreferenciación (`*`):** Accede al contenido de la celda de memoria a la que apunta el puntero.

```cpp
int x = 42;
int* ptr = &x; // ptr guarda la dirección de x
*ptr = 100;    // Modifica directamente el valor de x a 100
```

### Aritmética de Punteros:
Cuando incrementamos un puntero (`ptr++`), este no se incrementa en 1 byte físico. El compilador calcula automáticamente el salto en memoria basándose en el tipo de datos al que apunta (`sizeof(tipo)`).
* Si `ptr` es un puntero a `int` (4 bytes) y su dirección es `0x1000`, `ptr + 1` apuntará a la dirección `0x1004`.
* **Resta de Punteros:** Restar dos punteros del mismo tipo (ej: `ptr2 - ptr1`) devuelve el **número de elementos** entre ellos, no la diferencia en bytes físicos. Esto es sumamente útil para calcular índices relativos en un arreglo.

### Array Decay a fondo:
Cuando pasamos un arreglo a una función, este decae a un puntero. Esto significa que dentro de la función, hacer `sizeof(arreglo)` ya no nos da el tamaño total en bytes del arreglo entero, sino solo el tamaño del puntero en sí mismo (generalmente 8 bytes en arquitecturas de 64 bits).

---

## Retos del Día 6

### Reto 131: Manipulación Indirecta (Puntero Básico)
* **Archivo de plantilla:** `plantillas/reto_131.cpp`
* **Descripción:** Lee un entero `X`. Obtén su dirección de memoria en un puntero `int* ptr`. Incrementa el valor de la variable original sumándole 10 **únicamente a través del puntero** (`*ptr`). Imprime el nuevo valor de `X`.
* **Salida esperada:**
  ```text
  VALOR=<nuevo_valor>
  ```

### Reto 132: Recorrido con Punteros (`ptr++`)
* **Archivo de plantilla:** `plantillas/reto_132.cpp`
* **Descripción:** Lee `N` y luego `N` enteros. Implementa un bucle para sumar todos los elementos del arreglo usando aritmética de punteros: declara un puntero `int* ptr` que apunte al inicio del arreglo e increméntalo paso a paso (`ptr++`) en lugar de usar índices entre corchetes `[i]`.
* **Salida esperada:**
  ```text
  SUMA=<suma_total>
  ```

### Reto 133: Swap con Punteros
* **Archivo de plantilla:** `plantillas/reto_133.cpp`
* **Descripción:** Lee dos enteros `A` y `B`. Implementa una función `void mi_swap(int* a, int* b)` que intercambie el valor de las variables apuntadas usando desreferenciación. Invoca a la función en `main` pasándole las direcciones físicas de `A` y `B` (`&A`, `&B`).
* **Salida esperada:**
  ```text
  A=<nuevo_A>
  B=<nuevo_B>
  ```

### Reto 134: Prueba Empírica del Decay
* **Archivo de plantilla:** `plantillas/reto_134.cpp`
* **Descripción:** Declara en `main` un arreglo local `int arr[10];`. Implementa una función `int obtenerTamanoDecay(int arr[])` que devuelva el resultado de evaluar `sizeof(arr)` dentro de ella. Imprime tanto el tamaño medido en `main` como el tamaño medido en la función.
* **Salida esperada:**
  ```text
  LOCAL_SIZE=40
  DECAYED_SIZE=<tamano_de_un_puntero>
  ```
  *(Nota: `DECAYED_SIZE` será usualmente 8 en la mayoría de entornos de 64 bits).*

### Reto 135: Dirección del Elemento Máximo
* **Archivo de plantilla:** `plantillas/reto_135.cpp`
* **Descripción:** Lee `N` y luego `N` enteros. Implementa la función `const int* buscarMaximo(const int* arr, int tam)` que recorra el arreglo y devuelva la **dirección de memoria** (el puntero) del elemento con el valor más alto. En `main`, calcula y muestra el índice de dicho elemento restando los punteros (`puntero_maximo - arr`) y su valor.
* **Salida esperada:**
  ```text
  INDICE=<indice_del_maximo>
  VALOR=<valor_del_maximo>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_131.cpp soluciones/reto_131.cpp
# Resuelve soluciones/reto_131.cpp
python3 test_dia_6.py soluciones/reto_131.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_6.py all
```
