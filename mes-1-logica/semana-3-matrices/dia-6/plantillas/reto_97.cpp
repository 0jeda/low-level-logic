/*
 * Reto 97: Ordenar las Filas de una Matriz
 * Lee R, C y los R x C enteros.
 * Ordena cada fila ascendentemente con Insertion Sort.
 * 
 * Formato de salida:
 * MATRIZ=
 * <fila_0_ordenada>
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
    // Ordena cada fila usando Insertion Sort.
    // -----------------------------------------------------------------

    return 0;
}
