/*
 * Reto 42: Diferencia Máxima entre Dos Elementos
 * Lee N (2 <= N <= 1000) y N enteros.
 * Encuentra la máxima diferencia absoluta entre cualquier pareja.
 * 
 * Formato de salida:
 * DIFERENCIA=<valor>
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
    // Encuentra la diferencia máxima absoluta (puedes resolverlo en O(N)).
    // -----------------------------------------------------------------

    return 0;
}
