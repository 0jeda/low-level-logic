# Día 7: El Gran Reto Semanal y Git Básico

## Teoría: Uniendo la Aritmética de Bits y el Flujo de Git

Hoy culminamos la primera semana consolidando todo lo aprendido sobre tipos de datos, límites físicos, complementos binarios y manipulación a nivel de bits.

Además de resolver los desafíos de lógica de hoy, la última parte consiste en integrar tus soluciones en el repositorio usando el flujo de trabajo colaborativo real de **Git**.

### Repaso del Flujo de Git
Para consolidar tus ejercicios en GitHub y mantener tu historial limpio, debes seguir estos pasos desde la consola de Git en la raíz del proyecto:
1. Asegúrate de estar en una rama de solución limpia: `git checkout -b soluciones/semana-1-mi-nombre`.
2. Añade los archivos que modificaste: `git add mes-1-logica/semana-1-variables/dia-*/soluciones/reto_*.cpp`.
3. Haz un commit descriptivo: `git commit -m "feat(semana-1): resolver todos los retos del dia 1 al 7"`.
4. Sube la rama al servidor: `git push origin soluciones/semana-1-mi-nombre`.
5. Abre una **Pull Request (PR)** en GitHub para comparar tu código con la rama `main`.

---

## Retos del Día 7

### Reto 31: Contar Bits Encendidos (El Reto Semanal)
* **Archivo de plantilla:** `plantillas/reto_31.cpp`
* **Descripción:** Escribe un programa que reciba un número entero `N` y determine cuántos bits están encendidos (`1`) en su representación binaria de 32 bits, utilizando **únicamente operaciones de bits y un bucle**.
* **Salida esperada:**
  ```text
  BITS=<cantidad_de_unos>
  ```

### Reto 32: Potencia de Dos en Tiempo Constante $O(1)$
* **Archivo de plantilla:** `plantillas/reto_32.cpp`
* **Descripción:** Lee un número entero `N`. Determina si es una potencia de 2 (valores como 1, 2, 4, 8, 16, etc.) en tiempo constante $O(1)$.
* **Restricción:** Queda **estrictamente prohibido** usar bucles o llamadas recursivas. Debes resolverlo con una sola comprobación a nivel de bits.
* **Pista:** Si un número es potencia de dos, su representación binaria tiene exactamente un bit en `1`. ¿Qué ocurre si hacemos un AND lógico de `N` con `N - 1`?
* **Salida esperada:**
  - Si es potencia de 2: `POTENCIA=SI`
  - De lo contrario: `POTENCIA=NO`

### Reto 33: Racha de Bits Consecutivos en 1
* **Archivo de plantilla:** `plantillas/reto_33.cpp`
* **Descripción:** Lee un entero `N`. Encuentra la longitud de la racha (secuencia consecutiva) más larga de bits con valor `1` en su representación binaria.
* **Ejemplo:** `156` en binario es `10011100`. La racha más larga de unos consecutivos es `3` (los tres unos en el centro).
* **Salida esperada:**
  ```text
  RACHA=<longitud_de_la_racha>
  ```

### Reto 34: Inversión Completa de Bits (Bit Reversal)
* **Archivo de plantilla:** `plantillas/reto_34.cpp`
* **Descripción:** Lee un entero sin signo de 32 bits `N`. Invierte el orden de todos sus 32 bits (el bit 0 pasa a ser el bit 31, el bit 1 pasa a ser el bit 30, etc.) e imprime el valor decimal sin signo del número resultante.
* **Salida esperada:**
  ```text
  REVERSADO=<valor_decimal_resultante>
  ```

### Reto 35: Simulación de ALU de 1 bit
* **Archivo de plantilla:** `plantillas/reto_35.cpp`
* **Descripción:** Simula una Unidad Aritmético-Lógica (ALU) de 1 bit. Lee cinco enteros (`a`, `b`, `cin`, `op0`, `op1`), donde `a`, `b` y `cin` son bits individuales (0 o 1) y `op0`, `op1` seleccionan la operación de la ALU según la siguiente tabla:
  - `op0=0, op1=0`: Operación **AND** (`a & b`)
  - `op0=0, op1=1`: Operación **OR** (`a | b`)
  - `op0=1, op1=0`: Operación **XOR** (`a ^ b`)
  - `op0=1, op1=1`: Operación **SUMA COMPLETA** (Full Adder con entradas `a`, `b` y acarreo de entrada `cin`). Calcula el bit de resultado `res` y el acarreo de salida `cout`.
  *Para las operaciones que no sean SUMA, el acarreo de salida `cout` debe ser 0.*
* **Salida esperada:**
  ```text
  RES=<resultado>
  COUT=<cout>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_31.cpp soluciones/reto_31.cpp
# Edita soluciones/reto_31.cpp
python3 test_dia_7.py 31 soluciones/reto_31.cpp
```
O prueba todo tu set del Día 7:
```bash
python3 test_dia_7.py all
```
