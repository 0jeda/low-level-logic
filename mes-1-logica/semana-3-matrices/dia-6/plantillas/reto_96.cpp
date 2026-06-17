/*
 * Reto 96: Ordenar una Matriz Completa In-Place
 * Lee R, C (1 <= R, C <= 50) y la matriz R x C.
 * Ordena la matriz completa ascendentemente in-place usando O(1) espacio auxiliar.
 * 
 * Formato de salida:
 * MATRIZ=
 * <elementos fila 0 ordenados separados por espacio>
 * ...
 */

#include <iostream>

int main() {
    int R, C;
    if (!(std::cin >> R >> C)) return 1;

    int matriz[50][50];
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            std::cin >> matriz[i][j];
        }
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Ordena la matriz completa in-place usando mapeo a 1D.
    // -----------------------------------------------------------------

    return 0;
}
