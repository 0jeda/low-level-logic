/*
 * Reto 39: Inversión de Arreglo In-Place (O(1) en Espacio)
 * Lee N y N enteros.
 * Invierte el arreglo in-place (intercambiando extremos hacia el centro).
 * 
 * Formato de salida:
 * ARREGLO=<e1> <e2> ... <eN>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Invierte el arreglo en la misma memoria y luego imprímelo.
    // -----------------------------------------------------------------

    return 0;
}
