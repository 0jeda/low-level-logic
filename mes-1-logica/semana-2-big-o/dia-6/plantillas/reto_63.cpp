/*
 * Reto 63: Encontrar el Número Faltante
 * Lee N. Sigue un arreglo de tamaño N-1 con enteros en el rango [1, N].
 * Encuentra el número faltante en O(N) y O(1).
 * 
 * Formato de salida:
 * FALTANTE=<valor>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N - 1; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Encuentra el elemento faltante.
    // -----------------------------------------------------------------

    return 0;
}
