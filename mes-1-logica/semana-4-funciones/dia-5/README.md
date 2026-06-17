# Día 5: Funciones Puras e Inmutabilidad

## Teoría: Determinismo y Ausencia de Efectos Secundarios

En la ingeniería de software, una **función pura** es aquella que cumple estrictamente con dos condiciones:

1. **Determinismo:** Retorna siempre el mismo valor de salida para los mismos argumentos de entrada. No depende de ningún estado externo mutable (como variables globales o archivos en disco).
2. **Sin efectos secundarios (Side Effects):** No modifica ningún estado fuera de su propio ámbito local. Esto significa que no altera sus argumentos de entrada (inmutabilidad), no escribe en variables globales ni realiza operaciones de entrada/salida directas que alteren el sistema llamador.

```cpp
// Función Pura:
int suma(int a, int b) {
    return a + b;
}

// Función Impura (depende de variable global):
int g = 10;
int sumaImpura(int a) {
    return a + g;
}
```

### Beneficios de la Inmutabilidad:
* **Facilidad de prueba (Testability):** Son extremadamente sencillas de probar unitariamente.
* **Seguridad en Concurrencia (Thread-Safety):** Al no modificar memoria compartida, múltiples hilos de ejecución pueden llamarlas simultáneamente sin riesgo de condiciones de carrera (*Race Conditions*).
* **Optimizaciones del Compilador:** El compilador puede memorizar o reutilizar llamadas a funciones puras sabiendo que el resultado no cambiará (*Referential Transparency*).

---

## Retos del Día 5

### Reto 126: Detector de Primos (Puro)
* **Archivo de plantilla:** `plantillas/reto_126.cpp`
* **Descripción:** Lee un número `N`. Implementa la función pura `bool esPrimo(int n)` que determine si un número es primo. No uses variables globales ni alteres estados del programa.
* **Salida esperada:**
  ```text
  PRIMO=<0_o_1>
  ```

### Reto 127: Factorial Recursivo Puro
* **Archivo de plantilla:** `plantillas/reto_127.cpp`
* **Descripción:** Lee un entero `N` ($N \geq 0$). Implementa la función recursiva pura `long long factorial(int n)` para calcular el factorial.
* **Salida esperada:**
  ```text
  FACTORIAL=<resultado>
  ```

### Reto 128: Potencia Pura
* **Archivo de plantilla:** `plantillas/reto_128.cpp`
* **Descripción:** Lee un entero `A` (base) y `B` (exponente, $B \geq 0$). Implementa la función pura `long long potencia(int base, int exponente)` que calcule $A^B$ sin usar `std::pow`.
* **Salida esperada:**
  ```text
  POTENCIA=<resultado>
  ```

### Reto 129: Filtrado Inmutable de Pares
* **Archivo de plantilla:** `plantillas/reto_129.cpp`
* **Descripción:** Lee `N` enteros en un arreglo origen. Implementa la función pura `int filtrarPares(const int origen[], int tam, int destino[])` que filtre los números pares del arreglo `origen` y los guarde en `destino` sin modificar `origen`. Retorna la cantidad de pares guardados.
* **Salida esperada:**
  ```text
  PARES=[x1,x2,...,xm]
  ```

### Reto 130: Concatenador de Strings Puro
* **Archivo de plantilla:** `plantillas/reto_130.cpp`
* **Descripción:** Lee dos palabras (sin espacios). Implementa la función pura `void concatenar(const char str1[], const char str2[], char resultado[])` que reciba dos cadenas de caracteres de estilo C (terminadas en `\0`) y escriba su concatenación en el arreglo `resultado`, sin alterar las cadenas originales.
* **Salida esperada:**
  ```text
  CONCATENADO=<resultado_string>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_126.cpp soluciones/reto_126.cpp
# Resuelve soluciones/reto_126.cpp
python3 test_dia_5.py soluciones/reto_126.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_5.py all
```
