/*
 * Reto 88: Inserción de un Elemento Desalineado
 * Lee N (2 <= N <= 1000) y N enteros.
 * Los primeros N-1 elementos ya están ordenados. El último en arr[N-1] está desalineado.
 * Haz un único paso de inserción en O(N) para ordenar todo el arreglo.
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
    // Realiza un único desplazamiento e inserción del último elemento.
    // -----------------------------------------------------------------

    return 0;
}
