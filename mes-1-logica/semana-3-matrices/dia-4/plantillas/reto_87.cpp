/*
 * Reto 87: Insertion Sort Descendente
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma descendente usando Insertion Sort.
 * 
 * Formato de salida:
 * ORDENADO=<e1> <e2> ... <eN>
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
    // Ordena de forma descendente e imprime.
    // -----------------------------------------------------------------

    return 0;
}
