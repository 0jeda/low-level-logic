/*
 * Reto 81: Bubble Sort Estándar (Conteo de Intercambios)
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma ascendente con Bubble Sort estándar.
 * Cuenta la cantidad total de swaps realizados.
 * 
 * Formato de salida:
 * INTERCAMBIOS=<conteo>
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
    // Ordena e imprime los intercambios y el arreglo ordenado.
    // -----------------------------------------------------------------

    return 0;
}
