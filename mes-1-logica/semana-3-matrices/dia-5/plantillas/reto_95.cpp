/*
 * Reto 95: Puntos de Silla (Saddle Point)
 * Lee R, C, y los R x C enteros.
 * Encuentra un elemento mínimo en su fila y máximo en su columna.
 * 
 * Formato de salida:
 * SILLA=<valor> EN (<fila>,<columna>)
 * (o NINGUNO si no existe)
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
    // Busca el punto de silla e imprime.
    // -----------------------------------------------------------------

    return 0;
}
