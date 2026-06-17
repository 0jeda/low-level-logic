# Día 2: Ámbito de Variables y Gestión del Call Stack

## Teoría: Ámbitos, Duración y la Pila de Ejecución

Hoy profundizaremos en cómo el compilador y la CPU gestionan la visibilidad y el ciclo de vida de los datos.

### 1. Ámbito y Shadowing (Sombreado)
El **ámbito (scope)** de una variable es la región del código donde su nombre es válido y accesible. 
* **Global:** Declarada fuera de cualquier función. Visible en todo el archivo.
* **Local:** Declarada dentro de un bloque `{ ... }` (como una función o bucle). Solo visible dentro de ese bloque.
* **Shadowing:** Ocurre cuando declaramos una variable local con el mismo nombre que una variable global (o de un bloque superior). La variable local "oculta" a la global. En C++, podemos acceder a la variable global oculta usando el operador de resolución de ámbito (`::variable`).

```cpp
int x = 10; // Global

void func() {
    int x = 5; // Local (shadowing)
    std::cout << x;   // Imprime 5
    std::cout << ::x;  // Imprime 10 (accede a la global)
}
```

### 2. Variables Estáticas Locales (`static`)
Por defecto, las variables locales tienen **duración automática**: se crean cuando la ejecución entra a su bloque y se destruyen al salir. 
Si usamos la palabra clave `static`, la variable local adquiere **duración estática**: se inicializa solo la primera vez que se ejecuta la línea y **conserva su valor entre llamadas sucesivas** a la función, pero sigue siendo accesible únicamente desde dentro de esa función.

```cpp
int contador() {
    static int c = 0; // Se ejecuta una sola vez
    c++;
    return c;
}
```

### 3. Anatomía del Call Stack y Marcos de Pila
La **Pila de Llamadas (Call Stack)** es una región de memoria LIFO (Last In, First Out) gestionada por el hardware/sistema operativo. Cada vez que una función es invocada:
1. Se reserva un bloque de memoria llamado **Marco de Pila (Stack Frame)**.
2. Este frame almacena los parámetros de la función, sus variables locales y la **dirección de retorno** (dónde debe continuar la CPU cuando termine la función).
3. Al retornar, el Stack Frame se libera y la dirección de retorno se saca de la pila.

Si una función se llama a sí misma recursivamente sin una condición de parada adecuada, los frames se acumulan infinitamente hasta agotar el espacio físico reservado para la pila, produciendo un **Stack Overflow**.

---

## Retos del Día 2

### Reto 111: Acceso a Variables Sombreadas (Shadowing)
* **Archivo de plantilla:** `plantillas/reto_111.cpp`
* **Descripción:** Existe una variable global `int X = 100;`. Lee un valor `X` del usuario en `main` que sombreará a la variable global. Imprime los valores global y local por separado y calcula su suma.
* **Salida esperada:**
  ```text
  GLOBAL=<valor_global>
  LOCAL=<valor_local>
  SUMA=<suma_de_ambos>
  ```

### Reto 112: Contador de Visitas Estático
* **Archivo de plantilla:** `plantillas/reto_112.cpp`
* **Descripción:** Lee un entero `N` que indica cuántas veces llamarás a la función `void registrarPaso(int valor)`. En cada llamada, pasa un valor diferente que se sumará a una variable `static` acumuladora local. Además, mantén un contador `static` de llamadas. La función debe imprimir en cada llamada el estado actual.
* **Salida esperada por llamada:**
  ```text
  LLAMADA=<numero_de_llamada> SUMA=<suma_acumulada>
  ```

### Reto 113: Simulación Visual del Call Stack
* **Archivo de plantilla:** `plantillas/reto_113.cpp`
* **Descripción:** Lee un entero `X`. Implementa tres funciones de forma que `main` llame a `funcionA(X)`, esta llame a `funcionB(X - 1)`, y esta a su vez llame a `funcionC(X - 2)`. Cada función debe imprimir un mensaje al entrar y al salir para rastrear el comportamiento LIFO del stack de llamadas.
* **Salida esperada:**
  ```text
  ENTRA_A X=<valor>
  ENTRA_B X=<valor-1>
  ENTRA_C X=<valor-2>
  SALE_C X=<valor-2>
  SALE_B X=<valor-1>
  SALE_A X=<valor>
  ```

### Reto 114: Detector y Prevención de Stack Overflow
* **Archivo de plantilla:** `plantillas/reto_114.cpp`
* **Descripción:** Lee un número inicial `N` y un límite de profundidad `MAX_DEPTH`. Implementa una función recursiva `void recursiva(int n, int depth, int max_depth)` que decremente `n` en 1 en cada llamada. Si `depth` supera a `max_depth`, se debe detener la ejecución imprimiendo un aviso de desbordamiento prevenido.
* **Salida esperada:**
  * Si se previene el desbordamiento:
    ```text
    ... (impresiones previas de profundidad)
    STACK_OVERFLOW_PREVENIDO depth=<depth>
    ```
  * Si llega a `n == 0` antes del límite:
    ```text
    DEPTH=<depth> VALOR=<n>
    FIN n=0
    ```

### Reto 115: Solo Lectura con Referencias Constantes
* **Archivo de plantilla:** `plantillas/reto_115.cpp`
* **Descripción:** Lee un valor numérico `X` y un factor `F`. Implementa una función `int calcularFactor(const int &num, const int &factor)` que reciba ambos valores por referencia a constante. Como son de solo lectura, la función no puede modificarlos, pero debe calcular y retornar `num * factor`.
* **Salida esperada:**
  ```text
  ENTRADA=<num>
  FACTOR=<factor>
  RESULTADO=<num_por_factor>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_111.cpp soluciones/reto_111.cpp
# Resuelve soluciones/reto_111.cpp
python3 test_dia_2.py soluciones/reto_111.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_2.py all
```
