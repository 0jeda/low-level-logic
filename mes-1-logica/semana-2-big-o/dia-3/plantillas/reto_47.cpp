/*
 * Reto 47: Búsqueda Binaria Iterativa
 * Lee N, N enteros ordenados ascendentemente, y un objetivo T.
 * Implementa la búsqueda binaria en O(log N).
 * 
 * Formato de salida:
 * INDICE=<índice>   (o -1 si no se encuentra)
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
    // Implementa la búsqueda binaria iterativa.
    // -----------------------------------------------------------------

    return 0;
}
