/*
 * Reto 68: Intersección de Arreglos Ordenados (Dos Punteros)
 * Lee N, N enteros ordenados del primer arreglo.
 * Lee M, M enteros ordenados del segundo arreglo.
 * Encuentra la intersección en O(N + M) tiempo y O(1) espacio.
 * 
 * Formato de salida:
 * INTERSECCION=<e1> <e2> ...
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr1[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr1[i];
    }

    int M;
    if (!(std::cin >> M)) return 1;

    int arr2[1000];
    for (int i = 0; i < M; ++i) {
        std::cin >> arr2[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Halla la intersección usando dos punteros sin duplicados en la salida.
    // -----------------------------------------------------------------

    return 0;
}
