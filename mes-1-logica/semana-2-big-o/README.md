# Semana 2 – Introducción a la Complejidad Algorítmica (Big O) y Arreglos Lineales

¡Bienvenido/a a la segunda semana de **Low-Level Logic**!

Esta semana daremos un salto fundamental: dejaremos de preocuparnos únicamente por "cómo escribir código" y empezaremos a medir **cuán eficiente es nuestro código** antes de ejecutarlo.

---

## 📈 Conceptos Clave de la Semana

### 1. ¿Qué es la Notación Big O?
La **Notación Big O** es una herramienta matemática que describe el comportamiento de un algoritmo a medida que el tamaño de los datos de entrada (generalmente llamado $N$) crece hacia el infinito. Nos ayuda a medir:
* **Complejidad Temporal:** ¿Cuántas operaciones básicas realiza el algoritmo respecto a $N$?
* **Complejidad Espacial:** ¿Cuánta memoria adicional consume el algoritmo respecto a $N$?

### 2. Las Complejidades más Comunes
* **$O(1)$ (Tiempo Constante):** La velocidad no depende del tamaño de los datos. *Ejemplo: Acceder a un elemento de un arreglo por su índice.*
* **$O(\log N)$ (Tiempo Logarítmico):** El espacio de búsqueda se reduce a la mitad en cada paso. *Ejemplo: Búsqueda Binaria.*
* **$O(N)$ (Tiempo Lineal):** El tiempo crece de forma directamente proporcional al tamaño de los datos. *Ejemplo: Recorrer un arreglo una vez.*
* **$O(N^2)$ (Tiempo Cuadrático):** El algoritmo contiene bucles anidados. *Ejemplo: Comparar cada elemento contra todos los demás.*

### 3. Arreglos en Memoria de Bajo Nivel
Un **arreglo lineal (array)** es una secuencia de elementos del mismo tipo almacenados en **posiciones de memoria contiguas**.
* Gracias a la contigüidad, la CPU calcula la dirección física de cualquier índice instantáneamente mediante la fórmula:
  $$\text{Dirección} = \text{Dirección Base} + (\text{Índice} \times \text{Tamaño del Tipo de Dato})$$
* Este cálculo aritmético se realiza a nivel de hardware, lo que permite que el acceso indexado sea estrictamente $O(1)$ en tiempo.
* Sin embargo, insertar o eliminar elementos requiere desplazar la memoria contigua, lo que en el peor de los casos toma tiempo $O(N)$.

---

## 📅 Ruta de Retos Diarios

* **[Día 1: Arreglos Estáticos y Acceso Lineal ($O(N)$)](./dia-1/README.md)** (Retos 36 a 40)
* **[Día 2: Complejidad Cuadrática ($O(N^2)$) y Comparaciones](./dia-2/README.md)** (Retos 41 a 45)
* **[Día 3: Búsqueda Lineal vs. Búsqueda Binaria ($O(\log N)$)](./dia-3/README.md)** (Retos 46 a 50)
* **[Día 4: Optimización Espacial (Algoritmos In-Place $O(1)$)](./dia-4/README.md)** (Retos 51 a 55)
* **[Día 5: Ventanas Deslizantes y Subarreglos (Sliding Window)](./dia-5/README.md)** (Retos 56 a 60)
* **[Día 6: Complejidad Espacial y Arreglos de Frecuencia](./dia-6/README.md)** (Retos 61 a 65)
* **[Día 7: El Gran Reto de Búsqueda y Justificación de Big O](./dia-7/README.md)** (Retos 66 a 70)

---

## 🛠️ Instrucciones de Ejecución
Para empezar a trabajar en los retos de hoy, entra al directorio diario deseado:
```bash
cd mes-1-logica/semana-2-big-o/dia-1/
cp plantillas/reto_36.cpp soluciones/reto_36.cpp
# Edita tu archivo soluciones/reto_36.cpp
python3 test_dia_1.py soluciones/reto_36.cpp
```
