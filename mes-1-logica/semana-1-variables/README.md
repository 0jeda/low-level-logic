# Semana 1 – Variables, Tipos de Datos Estrictos y Operaciones de Bits

¡Bienvenido/a a la primera semana de entrenamiento de **Low-Level Logic**!

Esta semana el objetivo es **romper la abstracción** de los lenguajes de alto nivel y el pseudocódigo, comprendiendo que los datos ocupan un espacio físico real y finito en la memoria de la máquina.

---

## 📅 Estructura del Aprendizaje Diario

Hemos dividido esta semana en **7 días de entrenamiento intensivo**, con **5 retos prácticos por día** (un total de 35 desafíos). Cada día aborda un tema específico y avanza en complejidad:

1. **[Día 1: Enteros, Límites y Desbordamientos (Overflow)](./dia-1/README.md)**
   * Temas: `short`, `int`, `long long`, desbordamiento por exceso y defecto.
2. **[Día 2: Números de Punto Flotante y Precisión](./dia-2/README.md)**
   * Temas: `float`, `double`, IEEE 754, infinitos y NaN, errores de redondeo acumulativos.
3. **[Día 3: Caracteres, Booleanos y Tabla ASCII](./dia-3/README.md)**
   * Temas: `char` como tipo numérico, conversiones de caso, compuertas lógicas y empaquetado inicial.
4. **[Día 4: Operadores a Nivel de Bits Básicos](./dia-4/README.md)**
   * Temas: Lógica binaria pura (`&`, `|`, `^`, `~`), intercambio sin temporal con XOR y Complemento a Dos.
5. **[Día 5: Desplazamientos de Bits y Máscaras](./dia-5/README.md)**
   * Temas: Multiplicación/división binaria (`<<`, `>>`), extracción de bits y máscaras en rangos $O(1)$.
6. **[Día 6: Práctica Integrada de Bits y Tipos](./dia-6/README.md)**
   * Temas: Bit packing (empaquetado de caracteres), simetrías binarias y adición lógica (Half-Adder).
7. **[Día 7: El Gran Reto Semanal y Git Básico](./dia-7/README.md)**
   * Temas: Contar bits encendidos, evaluar potencias de dos, rachas consecutivas y simular una ALU de 1 bit.

---

## 🛠️ Cómo Trabajar en los Retos de Cada Día

1. **Entra en el directorio del día en el que vas a trabajar**:
   ```bash
   cd mes-1-logica/semana-1-variables/dia-N/
   ```
2. **Lee la teoría y la descripción de los 5 retos** en el `README.md` de ese día.
3. **Copia la plantilla** del reto que deseas resolver a la carpeta `soluciones/`:
   ```bash
   cp plantillas/reto_X.cpp soluciones/reto_X.cpp
   ```
4. **Escribe tu código** en `soluciones/reto_X.cpp` rellenando la sección `// TU CÓDIGO AQUÍ`.
5. **Prueba tu solución** ejecutando el script de pruebas automatizadas:
   ```bash
   python3 test_dia_N.py X soluciones/reto_X.cpp
   ```
   O bien, prueba todas tus soluciones acumuladas del día con:
   ```bash
   python3 test_dia_N.py all
   ```
   *(Donde `N` es el número de día del 1 al 7 y `X` es el número de reto del 1 al 35).*

---

> 💡 **Consejo:** No te saltes ningún día. Aunque los primeros retos parezcan sencillos, están diseñados para asentar las bases mecánicas y lógicas que necesitarás para abordar los operadores de bits y el gran reto del Día 7. ¡Mucho éxito!
