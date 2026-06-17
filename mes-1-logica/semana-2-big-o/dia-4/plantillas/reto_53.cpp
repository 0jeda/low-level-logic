/*
 * Reto 53: Combinar Dos Arreglos Ordenados (Merge)
 * Lee N, N enteros ordenados del primer arreglo.
 * Lee M, M enteros ordenados del segundo arreglo.
 * Combínalos en un arreglo ordenado en O(N + M).
 * 
 * Formato de salida:
 * COMBINADO=<e1> <e2> ... <e_N+M>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr1[500];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr1[i];
    }

    int M;
    if (!(std::cin >> M)) return 1;

    int arr2[500];
    for (int i = 0; i < M; ++i) {
        std::cin >> arr2[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Combina ambos arreglos usando dos punteros de lectura.
    // -----------------------------------------------------------------

    return 0;
}
