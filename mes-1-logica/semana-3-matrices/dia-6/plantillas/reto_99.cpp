/*
 * Reto 99: Ordenar la Diagonal Principal
 * Lee N (1 <= N <= 50) y la matriz cuadrada de N x N.
 * Ordena la diagonal principal ascendentemente in-place.
 * 
 * Formato de salida:
 * MATRIZ=
 * <fila_0_con_diagonal_ordenada>
 * ...
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int matriz[50][50];
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cin >> matriz[i][j];
        }
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Ordena la diagonal principal in-place.
    // -----------------------------------------------------------------

    return 0;
}
