# Día 3: Caracteres (`char`), Booleanos (`bool`) y Tabla ASCII

## Teoría: Caracteres como Números Ocultos

En C++, el tipo de dato `char` ocupa **1 byte (8 bits)** de memoria. Aunque lo usamos para guardar letras, dígitos y símbolos (como `'A'`, `'5'`, `'%'`), para la CPU un `char` no es más que un número entero pequeño (generalmente con signo, de $-128$ a $127$, o sin signo, de $0$ a $255$).

### La Tabla ASCII
La correspondencia entre cada símbolo visual y su valor numérico en memoria está definida por la **Tabla ASCII** (American Standard Code for Information Interchange). Por ejemplo:
* `'A'` equivale al número decimal $65$.
* `'a'` equivale al número decimal $97$ (exactamente $65 + 32$).
* `'0'` equivale al número decimal $48$ (no confundir el carácter `'0'` con el valor numérico `0`).

Dado que son números, podemos realizar operaciones aritméticas sobre caracteres:
```cpp
char letra = 'A';
letra = letra + 1; // letra ahora vale 'B' (66)
```

### El Tipo Booleano (`bool`)
El tipo `bool` representa valores de verdad: `true` (verdadero) o `false` (falso). En C++:
* Ocupa **1 byte** en memoria (aunque técnicamente solo se necesita 1 bit, el byte es la unidad mínima direccionable).
* El valor `false` equivale a `0`.
* El valor `true` equivale a `1` (o a cualquier valor distinto de cero cuando se convierte de entero a booleano).

---

## Retos del Día 3

### Reto 11: Desplazamiento ASCII Cíclico (Cifrado César)
* **Archivo de plantilla:** `plantillas/reto_11.cpp`
* **Descripción:** Lee un carácter `C` y un entero `K` (desplazamiento, que puede ser positivo o negativo). Cifra el carácter desplazando su código ASCII `K` posiciones.
* **Regla de oro:** Para que el resultado siempre sea un carácter imprimible común, restringimos el rango a los caracteres desde el espacio en blanco (ASCII 32) hasta la tilde o virgulilla `'~'` (ASCII 126). Hay un total de 95 caracteres imprimibles. Si el desplazamiento excede estos límites, debe dar la vuelta de forma circular (aritmética modular).
* **Salida esperada:**
  ```text
  CIFRADO=<carácter_resultante>
  ```

### Reto 12: Clasificador de Caracteres Manual
* **Archivo de plantilla:** `plantillas/reto_12.cpp`
* **Descripción:** Lee un único carácter `C`. Determina si es una letra mayúscula, una letra minúscula, un dígito numérico, u otro símbolo.
* **Restricción:** Queda terminantemente prohibido incluir la librería `<cctype>` o usar funciones como `isupper`, `islower` o `isdigit`. Debes hacer la clasificación manualmente evaluando los rangos numéricos ASCII del carácter.
* **Salida esperada:**
  - Si es mayúscula (A-Z): `MAYUSCULA`
  - Si es minúscula (a-z): `MINUSCULA`
  - Si es dígito (0-9): `DIGITO`
  - De lo contrario: `OTRO`

### Reto 13: Inversor de Mayúsculas/Minúsculas Aritmético
* **Archivo de plantilla:** `plantillas/reto_13.cpp`
* **Descripción:** Lee un carácter `C`. Si es una letra mayúscula, conviértela a minúscula. Si es minúscula, conviértela a mayúscula. Si es cualquier otro carácter, déjalo sin modificar.
* **Restricción:** Está prohibido usar funciones de biblioteca. Resuélvelo usando la diferencia numérica que existe entre las mayúsculas y las minúsculas en la tabla ASCII (el número mágico $32$).
* **Salida esperada:**
  ```text
  RESULTADO=<carácter_resultante>
  ```

### Reto 14: Simulador de Compuertas Lógicas
* **Archivo de plantilla:** `plantillas/reto_14.cpp`
* **Descripción:** Lee dos valores enteros `A` y `B` (que serán `0` para falso o `1` para verdadero), seguidos de una cadena de texto `OP` que representa una operación lógica (`AND`, `OR`, `XOR`, `NAND`, `NOR`). Calcula el resultado lógico e imprímelo como `0` o `1`.
* **Salida esperada:**
  ```text
  LOGICA=<0 | 1>
  ```

### Reto 15: Empaquetador de Bits a Byte
* **Archivo de plantilla:** `plantillas/reto_15.cpp`
* **Descripción:** Lee 8 valores booleanos (como `0` o `1`) correspondientes a los bits de un byte, desde el más significativo (Bit 7, el primero que se lee) hasta el menos significativo (Bit 0, el último que se lee). Calcula el valor decimal final que representa dicho byte.
* **Ejemplo:** Si ingresan `1 0 0 0 0 0 0 1`, la salida es `VALOR=129` (ya que $2^7 + 2^0 = 128 + 1 = 129$).
* **Salida esperada:**
  ```text
  VALOR=<valor_decimal_del_byte>
  ```

---

## Cómo Ejecutar las Pruebas

```bash
cp plantillas/reto_11.cpp soluciones/reto_11.cpp
# Edita soluciones/reto_11.cpp
python3 test_dia_3.py 11 soluciones/reto_11.cpp
```
O prueba todo tu avance del día usando:
```bash
python3 test_dia_3.py all
```
