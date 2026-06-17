/*
 * Reto 66: Búsqueda Binaria en un Arreglo Rotado
 * Lee N, N enteros (ordenados y rotados), y T.
 * Encuentra el índice de T en O(log N) tiempo.
 * 
 * Formato de salida:
 * INDICE=<índice_encontrado_o_-1>
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
    // Implementa la búsqueda binaria en arreglo rotado.
    // -----------------------------------------------------------------

    return 0;
}
