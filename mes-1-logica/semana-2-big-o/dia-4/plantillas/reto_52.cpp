/*
 * Reto 52: Mover Ceros al Final
 * Lee N y N enteros.
 * Mueve los ceros al final manteniendo el orden relativo en O(N) y O(1).
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
    // Reubica los ceros al final del arreglo de forma estable.
    // -----------------------------------------------------------------

    return 0;
}
