/*
 * Reto 49: Punto de Inserción Correcto (lower_bound)
 * Lee N, N enteros ordenados ascendentemente, y T.
 * Encuentra el índice de inserción de T en O(log N).
 * 
 * Formato de salida:
 * INDICE=<índice>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int T;
    std::cin >> T;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Encuentra el punto de inserción (lower_bound) de T.
    // -----------------------------------------------------------------

    return 0;
}
