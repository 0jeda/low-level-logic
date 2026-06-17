/*
 * Reto 71: Suma de Filas y Columnas
 * Lee R, C, y los R x C enteros de la matriz.
 * Calcula la suma de cada fila y la suma de cada columna.
 * 
 * Formato de salida:
 * FILAS=<sF0> <sF1> ... <sFR-1>
 * COLUMNAS=<sC0> <sC1> ... <sCC-1>
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
    // Calcula la suma de cada fila y columna e imprímelas.
    // -----------------------------------------------------------------

    return 0;
}
