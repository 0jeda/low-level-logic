/*
 * Reto 74: Máximo y Mínimo en Matriz
 * Lee R, C, y los R x C enteros.
 * Encuentra el máximo y mínimo con sus coordenadas de fila y columna (0-indexado).
 * 
 * Formato de salida:
 * MAX=<valor> EN (<fila>,<columna>)
 * MIN=<valor> EN (<fila>,<columna>)
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
    // Encuentra máximo y mínimo con sus coordenadas.
    // -----------------------------------------------------------------

    return 0;
}
