/*
 * Reto 86: Insertion Sort Estándar (Conteo de Desplazamientos)
 * Lee N (1 <= N <= 1000) y N enteros.
 * Ordena de forma ascendente con Insertion Sort.
 * Cuenta la cantidad total de desplazamientos de celdas realizados.
 * 
 * Formato de salida:
 * DESPLAZAMIENTOS=<conteo>
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
    // Ordena con Insertion Sort y cuenta los desplazamientos.
    // -----------------------------------------------------------------

    return 0;
}
