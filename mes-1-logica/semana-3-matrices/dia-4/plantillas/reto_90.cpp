/*
 * Reto 90: Ordenamiento por Inserción Binaria (Binary Insertion Sort)
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma ascendente usando búsqueda binaria para hallar el punto de inserción.
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
    // Implementa el algoritmo Binary Insertion Sort.
    // -----------------------------------------------------------------

    return 0;
}
