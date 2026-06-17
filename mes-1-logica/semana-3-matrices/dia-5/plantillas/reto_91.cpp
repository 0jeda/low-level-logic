/*
 * Reto 91: Búsqueda en Matriz Ordenada 2D (Stepwise Search)
 * Lee R, C, los R x C enteros de la matriz ordenada, y T.
 * Busca T en O(R + C) comenzando desde la esquina superior derecha.
 * 
 * Formato de salida:
 * POSICION=(<fila>,<columna>)
 * (o ERROR si no existe)
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

    int T;
    std::cin >> T;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Busca T en O(R + C) e imprime.
    // -----------------------------------------------------------------

    return 0;
}
