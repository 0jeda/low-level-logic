# Día 1: Paso por Valor vs. Paso por Referencia

## Teoría: Copia Física vs. Alias de Memoria

Cuando llamamos a una función en C++, debemos decidir cómo viajan los datos hacia ella. C++ ofrece dos mecanismos principales:

### 1. Paso por Valor
Es el comportamiento por defecto. C++ reserva una nueva celda de memoria en el Stack Frame de la función y **copia físicamente** el valor de la variable de entrada.
* **Aislamiento:** La función no puede alterar la variable original en `main`.
* **Costo:** Para tipos primitivos como `int` es muy rápido, pero copiar estructuras grandes (como matrices) duplica el consumo de RAM.

```cpp
void duplicar(int x) { // x es una copia
    x = x * 2;
}
```

### 2. Paso por Referencia (`&`)
Al colocar el operador `&` en la declaración del parámetro, le decimos a C++ que no copie el dato. En su lugar, el parámetro se convierte en un **alias** o referencia directa a la dirección de memoria original.
* **Efecto lateral:** Cualquier modificación dentro de la función altera la variable original.
* **Eficiencia:** Es extremadamente rápido porque no copia memoria, solo transfiere la dirección.

```cpp
void duplicar(int &x) { // x es un alias directo
    x = x * 2;
}
```

---

## Retos del Día 1

### Reto 106: Duplicador por Valor y Referencia
* **Archivo de plantilla:** `plantillas/reto_106.cpp`
* **Descripción:** Lee un entero `X`. Implementa dos funciones:
  1. `void duplicarValor(int x)`: que multiplica el parámetro por 2.
  2. `void duplicarReferencia(int &x)`: que multiplica el parámetro por 2.
  * Muestra el valor de `X` después de llamar a cada función.
* **Salida esperada:**
  ```text
  VALOR=<valor_después_de_duplicarValor>
  REFERENCIA=<valor_después_de_duplicarReferencia>
  ```

### Reto 107: Intercambio con Referencias (Swap)
* **Archivo de plantilla:** `plantillas/reto_107.cpp`
* **Descripción:** Lee dos enteros `A` y `B`. Implementa una función `void mi_swap(int &a, int &b)` que intercambie sus valores usando referencias. Llama a la función desde `main` e imprime los valores actualizados de `A` y `B`.
* **Salida esperada:**
  ```text
  A=<nuevo_A>
  B=<nuevo_B>
  ```

### Reto 108: División y Módulo Simultáneos
* **Archivo de plantilla:** `plantillas/reto_108.cpp`
* **Descripción:** Lee un dividendo `A` y un divisor `B`. Implementa una función `void dividir(int dividendo, int divisor, int &cociente, int &resto)` que calcule la división entera y el módulo, y devuelva ambos resultados modificando las variables pasadas por referencia.
* **Salida esperada:**
  ```text
  COCIENTE=<cociente>
  RESTO=<resto>
  ```

### Reto 109: Limitador de Rango (Clamp por Referencia)
* **Archivo de plantilla:** `plantillas/reto_109.cpp`
* **Descripción:** Lee un entero `X`, un valor mínimo `min_val` y un valor máximo `max_val`. Implementa una función `void clamp(int &val, int min_lim, int max_lim)` que modifique por referencia `val` forzándolo a estar dentro del rango `[min_lim, max_lim]` (si es menor que `min_lim` se ajusta al mínimo, si es mayor que `max_lim` se ajusta al máximo).
* **Salida esperada:**
  ```text
  CLAMPED=<valor_resultante>
  ```

### Reto 110: Post-Incremento por Referencia
* **Archivo de plantilla:** `plantillas/reto_110.cpp`
* **Descripción:** Lee un entero `X` y un incremento `S`. Implementa una función `int postIncrementar(int &value, int step)` que incremente `value` en la cantidad `step` por referencia, pero retorne el **valor anterior** que tenía la variable antes de ser incrementada.
* **Salida esperada:**
  ```text
  RETORNADO=<valor_antes_de_la_suma>
  NUEVO=<valor_después_de_la_suma>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_106.cpp soluciones/reto_106.cpp
# Resuelve soluciones/reto_106.cpp
python3 test_dia_1.py 106 soluciones/reto_106.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_1.py all
```
