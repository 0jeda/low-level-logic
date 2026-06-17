/*
 * Reto 46: Búsqueda Lineal Estándar
 * Lee N, N enteros desordenados, y un objetivo T.
 * Encuentra el índice de la primera aparición de T.
 * 
 * Formato de salida:
 * INDICE=<índice>   (o -1 si no se encuentra)
 */

#include <iostream>

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
    // Busca T linealmente.
    // -----------------------------------------------------------------

    return 0;
}
