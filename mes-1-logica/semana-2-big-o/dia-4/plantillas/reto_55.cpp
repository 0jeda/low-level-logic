/*
 * Reto 55: Algoritmo de Votación de Boyer-Moore
 * Lee N (1 <= N <= 1000) y N enteros.
 * Encuentra el elemento mayoritario (que aparece > N/2 veces) en O(N) y O(1).
 * 
 * Formato de salida:
 * MAYORITARIO=<valor>
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
    // Implementa el algoritmo de votación de Boyer-Moore.
    // -----------------------------------------------------------------

    return 0;
}
