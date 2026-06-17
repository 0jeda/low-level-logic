/*
 * Reto 83: Bubble Sort Descendente
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma descendente (de mayor a menor) con Bubble Sort.
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
    // Ordena en forma descendente e imprime el arreglo.
    // -----------------------------------------------------------------

    return 0;
}
