# 🧠 Low-Level Logic: Reinicio de Fundamentos y Pensamiento Algorítmico

¡Bienvenido/a a **Low-Level Logic**! 

Este repositorio es un espacio de entrenamiento autónomo, intensivo y de código abierto diseñado para **romper los vicios de la academia tradicional y aprender a programar de verdad**. Si sientes que los planes de estudio universitarios se quedan en la superficie o abusan del pseudocódigo sin enseñarte el impacto real de tus decisiones en la máquina, este proyecto es para ti.

Aquí nos enfocamos en desarrollar el músculo del pensamiento lógico puro y duro utilizando **C/C++** como lenguaje base y **Python** como herramienta de automatización para pruebas locales.

---

##  Filosofía del Proyecto

* **Sin ruedas de entrenamiento:** Está estrictamente prohibido el uso de librerías avanzadas o métodos mágicos de alto nivel (como `std::sort`, estructuras dinámicas automatizadas, etc.). Todo se construye desde cero (bucles, control de flujo, algoritmos de ordenamiento a mano).
* **Git desde el primer día:** No subimos archivos sueltos. Cada reto se resuelve en una rama independiente y se integra mediante un flujo real de *Pull Requests*.
* **Criterio de Eficiencia:** No basta con que el código "corra". Aprendemos a evaluar el impacto en memoria y tiempo de ejecución usando **Notación Big O** (Complejidad Algorítmica).
* **Automatización Profesional:** Cada reto cuenta con un script de prueba en Python (`test_logica.py`) que compila tu código con `g++` y valida la solución localmente con múltiples casos de prueba antes de que envíes tu revisión.

---

## Mapa de Ruta (Roadmap de 2 Meses)

###  Mes 1: El Control Absoluto de la Lógica y la Eficiencia
* **Semana 1: Variables y Control de Flujo Básico** * El impacto de la asignación en memoria y operaciones aritméticas puras sin variables auxiliares.
* **Semana 2: Arreglos Lineales y Complejidad Algorítmica (Big O)**
  * Búsqueda Lineal vs. Búsqueda Binaria. Aprendiendo a medir la eficiencia en tiempo $O(\log n)$.
* **Semana 3: Matrices (2D) y Algoritmos de Ordenamiento Puro**
  * Movimiento de datos multidimensionales e implementación a mano de *Bubble Sort* o *Insertion Sort*.
* **Semana 4: Modularidad Extrema y Control del Call Stack**
  * Funciones puras y el uso estricto de paso de parámetros por referencia (`&`) para el control de memoria.

###  Mes 2: Abstracción, Estructuras y Recursividad
* **Semana 5: Modelado de Datos con Estructuras (`struct`)**
  * Agrupación de tipos de datos primitivos para resolver problemas del mundo real.
* **Semana 6: Pensamiento Inductivo y Recursividad Lineal**
  * Rompiendo la dependencia de los bucles cíclicos. El control del *Stack Overflow*.
* **Semana 7: Recursividad Avanzada y Optimización**
  * Estrategia de Divide y Vencerás mediante la implementación de *Merge Sort*.
* **Semana 8: Proyecto Integrador de Fin de Curso**
  * Desarrollo de un motor de búsqueda de texto básico en consola con Big O optimizado.

---

##  ¿Cómo empezar a resolver los retos? (Flujo de Trabajo Abierto)

Para mantener el repositorio limpio y permitir que múltiples usuarios resuelvan los retos al mismo tiempo sin pisarse el código, seguimos un flujo estricto de Git:

### 1. Clonar el repositorio y crear una rama propia
Nunca trabajes directamente sobre la rama `main`. Clona el proyecto y crea una rama con tu nombre y el reto de la semana:
```bash
git clone [https://github.com/TU_USUARIO/low-level-logic.git](https://github.com/TU_USUARIO/low-level-logic.git)
cd low-level-logic
git checkout -b solucion/semana-1-tu-nombre
