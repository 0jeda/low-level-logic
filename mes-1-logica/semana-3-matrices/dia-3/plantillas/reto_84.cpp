/*
 * Reto 84: Bubble Sort Bidireccional (Cocktail Shaker Sort)
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma ascendente usando Cocktail Shaker Sort.
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
    // Implementa Cocktail Shaker Sort.
    // -----------------------------------------------------------------

    return 0;
}
