/*
 * Reto 57: Subarreglo Más Corto con Suma Objetivo
 * Lee N, N enteros positivos, y un objetivo S.
 * Encuentra la longitud mínima de un subarreglo continuo cuya suma sea >= S.
 * Si no existe tal subarreglo, imprime 0.
 * 
 * Formato de salida:
 * MIN_LONGITUD=<valor>
 */

#include <iostream>
#include <algorithm> // Puedes usar std::min a mano o con la librería

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int S;
    std::cin >> S;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Encuentra la longitud mínima de subarreglo cuya suma >= S en O(N) tiempo.
    // -----------------------------------------------------------------

    return 0;
}
