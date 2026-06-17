/*
 * Reto 56: Suma Máxima de Subarreglo de Tamaño Fijo K
 * Lee N, N enteros, y K.
 * Encuentra la suma máxima de un subarreglo continuo de tamaño K en O(N).
 * 
 * Formato de salida:
 * MAX_SUMA=<valor>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int K;
    std::cin >> K;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Encuentra la suma máxima de un subarreglo de tamaño K usando sliding window.
    // -----------------------------------------------------------------

    return 0;
}
