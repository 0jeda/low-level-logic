/*
 * Reto 98: Ordenar las Columnas de una Matriz
 * Lee R, C y los R x C enteros.
 * Ordena cada columna ascendentemente.
 * 
 * Formato de salida:
 * MATRIZ=
 * <fila_0_con_columnas_ordenadas>
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
    // Ordena cada columna independientemente.
    // -----------------------------------------------------------------

    return 0;
}
