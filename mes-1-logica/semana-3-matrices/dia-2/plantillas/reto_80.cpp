/*
 * Reto 80: Espejo Horizontal In-Place
 * Lee R, C, y los R x C enteros.
 * Invierte horizontalmente cada fila in-place.
 * 
 * Formato de salida:
 * ESPEJO=
 * <fila_0_espejada>
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
    // Invierte cada fila in-place e imprime la matriz resultante.
    // -----------------------------------------------------------------

    return 0;
}
