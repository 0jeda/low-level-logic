/*
 * Reto 102: Rotación de Matriz 90 Grados Antihorario In-Place
 * Lee N (1 <= N <= 50) y la matriz cuadrada de N x N.
 * Rota la matriz 90 grados en sentido antihorario in-place.
 * 
 * RESTRICCIÓN:
 * No uses una segunda matriz auxiliar.
 * 
 * Formato de salida:
 * ROTADA=
 * <fila_0_rotada>
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
    // Rota la matriz 90 grados en sentido antihorario.
    // -----------------------------------------------------------------

    return 0;
}
