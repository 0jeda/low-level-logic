# Semana 1 – Variables y Tipos de Datos

## Teoría: ¿Qué es una variable en C++?

Una **variable** es un espacio con nombre en la memoria del computador que almacena un valor que puede cambiar durante la ejecución del programa.

En C++ cada variable tiene un **tipo de dato** que le dice al compilador cuánta memoria reservar y qué clase de valores puede guardar. Los más básicos son:

| Tipo    | Tamaño típico | Ejemplo de valor |
|---------|---------------|------------------|
| `int`   | 4 bytes       | `-3`, `0`, `42`  |
| `float` | 4 bytes       | `3.14`, `-0.5`   |
| `double`| 8 bytes       | `2.718281828`    |
| `char`  | 1 byte        | `'A'`, `'z'`     |
| `bool`  | 1 byte        | `true`, `false`  |

### Declaración y asignación

```cpp
int edad = 20;      // declaración con inicialización
float precio;       // declaración sin inicialización (valor indefinido)
precio = 9.99f;     // asignación posterior
```

### Operaciones aritméticas básicas

| Operador | Significado       | Ejemplo          |
|----------|-------------------|------------------|
| `+`      | Suma              | `a + b`          |
| `-`      | Resta             | `a - b`          |
| `*`      | Multiplicación    | `a * b`          |
| `/`      | División          | `a / b`          |
| `%`      | Módulo (resto)    | `a % b`          |

> **Regla importante:** Cuando ambos operandos son `int`, la división `/` descarta la parte decimal. Para obtener decimales al menos uno de los dos debe ser `float` o `double`.

---

## Reto 1 – El Intercambio de Variables

### Descripción

Escribe un programa en C++ que:

1. Lea **dos números enteros** (`A` y `B`) desde la entrada estándar (`std::cin`).
2. **Intercambie** sus valores: `A` debe tomar el valor original de `B` y `B` debe tomar el valor original de `A`.
3. Imprima el resultado por consola en el siguiente formato exacto:

```
A=<nuevo_valor_de_A>
B=<nuevo_valor_de_B>
```

**Ejemplo:**
```
Entrada: 5 10
Salida:
A=10
B=5
```

---

### ⚠️ RESTRICCIÓN DE LÓGICA (obligatoria)

> Está **estrictamente prohibido** usar una tercera variable auxiliar (`temporal`, `aux`, `tmp`, o cualquier variable adicional).
>
> El intercambio **debe resolverse únicamente con aritmética básica**: sumas y restas sobre las mismas dos variables `A` y `B`.

Esto significa que tu solución no puede contener ninguna declaración de variable extra más allá de `int A` e `int B`.

---

### 📚 Librerías permitidas

Solo se permite incluir:

```cpp
#include <iostream>
```

Queda prohibido el uso de `<algorithm>`, `<utility>`, `std::swap()`, o cualquier función de la biblioteca estándar que haga el intercambio por ti.

---

## Cómo Trabajar en este Reto

### 1. Crea tu propia rama

Desde la raíz del repositorio, crea una rama con tu nombre de usuario de GitHub:

```bash
git checkout -b soluciones/tu_usuario
```

### 2. Copia la plantilla a tu carpeta personal

```bash
# Situado en mes-1-logica/semana-1-variables/
cp plantilla.cpp soluciones/tu_nombre.cpp
```

> La carpeta `soluciones/` ya está creada con un `.gitkeep`. Nunca modifiques `plantilla.cpp` directamente.

### 3. Escribe tu solución

Abre `soluciones/tu_nombre.cpp` en tu editor favorito y completa el código donde dice `// TU CÓDIGO AQUÍ`.

### 4. Compila manualmente (opcional)

```bash
g++ -O2 -o mi_solucion soluciones/tu_nombre.cpp
./mi_solucion
```

### 5. Ejecuta las pruebas automáticas

```bash
python3 test_logica.py soluciones/tu_nombre.cpp
```

Si todos los casos pasan verás:

```
[OK] Caso 1: A=5, B=10  ->  A=10, B=5
[OK] Caso 2: A=-3, B=7  ->  A=7, B=-3
[OK] Caso 3: A=0, B=0   ->  A=0, B=0
[OK] Caso 4: A=100, B=-100 -> A=-100, B=100
✅ ¡Todos los casos de prueba pasaron!
```

### 6. Sube tu solución con un Pull Request

```bash
git add soluciones/tu_nombre.cpp
git commit -m "feat(semana-1): solución de tu_nombre para El Intercambio"
git push origin soluciones/tu_usuario
```

Luego abre un Pull Request desde GitHub apuntando a `main`. Los revisores usarán el mismo script de pruebas para validarla.

---

> 💡 **Tip:** Si tu programa compila pero los números no se intercambian correctamente, revisa el orden de las operaciones. La aritmética tiene un orden lógico que debes respetar.
