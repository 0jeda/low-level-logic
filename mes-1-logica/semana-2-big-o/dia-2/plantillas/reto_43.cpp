/*
 * Reto 43: Intersección de Arreglos No Ordenados
 * Lee N, N enteros del primer arreglo.
 * Lee M, M enteros del segundo arreglo.
 * Encuentra los elementos en común en el orden del primer arreglo sin duplicados.
 * 
 * Formato de salida:
 * INTERSECCION=<e1> <e2> ...
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
    // Encuentra la intersección e imprímela.
    // -----------------------------------------------------------------

    return 0;
}
