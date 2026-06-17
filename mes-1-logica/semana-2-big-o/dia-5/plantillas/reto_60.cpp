/*
 * Reto 60: Algoritmo de Kadane (Suma Máxima)
 * Lee N (1 <= N <= 1000) y N enteros (mixtos).
 * Encuentra la suma máxima de un subarreglo continuo en O(N) tiempo y O(1) espacio.
 * 
 * Formato de salida:
 * MAX_KADANE=<valor>
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
    // Implementa el algoritmo de Kadane e imprime el resultado.
    // -----------------------------------------------------------------

    return 0;
}
