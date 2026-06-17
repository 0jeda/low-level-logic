/*
 * Reto 50: Raíz Cuadrada Entera por Búsqueda Binaria
 * Lee un long long X (0 <= X <= 10^12).
 * Encuentra el mayor entero y tal que y^2 <= X usando búsqueda binaria.
 * 
 * RESTRICCIÓN:
 * No uses <cmath>, std::sqrt o tipos flotantes (float/double).
 * Todo en enteros y en O(log X).
 * 
 * Formato de salida:
 * RAIZ=<valor>
 */

#include <iostream>

int main() {
    long long X;
    if (!(std::cin >> X)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Realiza la búsqueda binaria sobre el rango de respuestas [0, X]
    // usando long long para prevenir desbordamientos en multiplicaciones.
    // -----------------------------------------------------------------

    return 0;
}
