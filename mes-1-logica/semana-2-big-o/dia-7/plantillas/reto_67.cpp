/*
 * Reto 67: Encontrar el Elemento Más Cercano
 * Lee N, N enteros ordenados ascendentemente, y T.
 * Encuentra el elemento del arreglo más cercano a T en O(log N).
 * 
 * Formato de salida:
 * CERCANO=<valor>
 */

#include <iostream>
#include <cmath> // Puedes usar std::abs para calcular distancias

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
    // Encuentra el elemento con valor más cercano a T en O(log N) tiempo.
    // -----------------------------------------------------------------

    return 0;
}
