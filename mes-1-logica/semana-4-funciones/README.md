# Semana 4 – Modularidad Extrema (Funciones y Paso de Parámetros)

¡Bienvenido/a a la cuarta y última semana del **Mes 1: El Control Absoluto de la Lógica y la Eficiencia**!

Esta semana integraremos todo lo aprendido sobre tipos de datos, bits, arreglos y matrices para construir programas modulares y limpios, mientras comprendemos cómo la CPU gestiona el flujo de control mediante la **Pila de Llamadas (Call Stack)** y el movimiento físico de datos.

---

## 📈 Conceptos Clave de la Semana

### 1. Paso por Valor vs. Paso por Referencia
* **Paso por Valor:** C++ crea una copia física del dato y se la pasa a la función. Cualquier modificación dentro de la función afecta únicamente a la copia, no a la variable original.
* **Paso por Referencia (`&`):** C++ pasa un alias o referencia directa a la celda de memoria original. Cualquier cambio dentro de la función altera la variable original de forma inmediata. Además, **evita duplicar memoria en RAM** al trabajar con estructuras grandes como matrices.

### 2. La Pila de Llamadas (Call Stack)
La **Pila de Llamadas** es la estructura de datos que utiliza la CPU para gestionar el flujo de ejecución de las funciones:
* Cada vez que se llama a una función, se añade un **Marco de Pila (Stack Frame)** con sus variables locales y la dirección de retorno.
* Cuando la función termina (`return`), su Stack Frame se destruye y el control vuelve a la función llamadora.
* Si una función se llama a sí misma de forma recursiva infinita o con demasiada profundidad, la memoria asignada a la pila se agota, provocando un **Stack Overflow** (Desbordamiento de Pila).

### 3. Punteros y la Decadencia de Arreglos (Array Decay)
En C++, cuando pasas un arreglo como parámetro a una función (ej: `void func(int arr[])`), el compilador no copia el arreglo completo. En su lugar, el arreglo decae implícitamente a un **puntero** (`int* arr`) que almacena únicamente la dirección del primer elemento. Esto significa que los arreglos siempre se pasan por referencia a nivel físico.

---

## 📅 Ruta de Retos Diarios

* **[Día 1: Paso por Valor vs. Paso por Referencia](./dia-1/README.md)** (Retos 106 a 110)
* **[Día 2: Ámbito de Variables y Gestión del Call Stack](./dia-2/README.md)** (Retos 111 a 115)
* **[Día 3: Paso de Arreglos 1D a Funciones](./dia-3/README.md)** (Retos 116 a 120)
* **[Día 4: Paso de Matrices (2D) a Funciones](./dia-4/README.md)** (Retos 121 a 125)
* **[Día 5: Funciones Puras e Inmutabilidad](./dia-5/README.md)** (Retos 126 a 130)
* **[Día 6: Punteros y la Relación con los Arreglos](./dia-6/README.md)** (Retos 131 a 135)
* **[Día 7: El Gran Reto - Calculadora de Álgebra Lineal](./dia-7/README.md)** (Retos 136 a 140)

---

## 🛠️ Instrucciones de Trabajo
Entra al subdirectorio correspondiente para comenzar el día:
```bash
cd mes-1-logica/semana-4-funciones/dia-1/
cp plantillas/reto_106.cpp soluciones/reto_106.cpp
# Edita soluciones/reto_106.cpp
python3 test_dia_1.py soluciones/reto_106.cpp
```
