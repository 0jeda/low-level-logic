/*
 * Reto 48: Primera Ocurrencia de un Duplicado
 * Lee N, N enteros ordenados (con posibles duplicados), y T.
 * Encuentra el primer índice de T (el de más a la izquierda).
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
    // Implementa la búsqueda binaria modificada para hallar la primera ocurrencia.
    // -----------------------------------------------------------------

    return 0;
}
