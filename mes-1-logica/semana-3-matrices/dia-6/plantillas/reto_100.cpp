/*
 * Reto 100: Búsqueda Binaria en Matriz Totalmente Ordenada
 * Lee R, C, los R x C enteros de la matriz ordenada, y T.
 * Realiza búsqueda binaria 2D en O(log(R * C)).
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
    // Implementa la búsqueda binaria 2D.
    // -----------------------------------------------------------------

    return 0;
}
