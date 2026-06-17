/*
 * Reto 101: Tablero de Buscaminas (Vecindad de Minas)
 * Lee R, C (1 <= R, C <= 50) y la matriz R x C.
 * Donde -1 es una mina y 0 es vacía.
 * Para cada 0, calcula y guarda el número de minas vecinas.
 * 
 * Formato de salida:
 * TABLERO=
 * <fila 0 separados por espacio>
 * ...
 */

#include <iostream>

int main() {
    int R, C;
    if (!(std::cin >> R >> C)) return 1;

    int tablero[50][50];
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            std::cin >> tablero[i][j];
        }
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Rellena las celdas vacías con el número de minas vecinas.
    // -----------------------------------------------------------------

    return 0;
}
