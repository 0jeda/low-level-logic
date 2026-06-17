/*
 * Reto 92: Fila con Más Ceros
 * Lee R, C, y los R x C enteros binarios (0s y 1s, ordenados por fila).
 * Encuentra la fila con más ceros en O(R + C) o O(R log C).
 * 
 * Formato de salida:
 * FILA=<fila>
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
    // Encuentra la fila con mayor número de ceros.
    // -----------------------------------------------------------------

    return 0;
}
