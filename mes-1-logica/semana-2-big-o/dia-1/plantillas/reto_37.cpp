/*
 * Reto 37: Máximo y Mínimo en un Solo Recorrido
 * Lee N (1 <= N <= 1000) y N enteros.
 * Encuentra el máximo y mínimo en un solo recorrido.
 * 
 * Formato de salida:
 * MAX=<valor>
 * MIN=<valor>
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
    // Encuentra el máximo y el mínimo en una sola pasada.
    // -----------------------------------------------------------------

    return 0;
}
