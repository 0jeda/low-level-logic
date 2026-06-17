/*
 * Reto 77: Recorrido en Espiral
 * Lee R, C, y los R x C enteros.
 * Imprime los elementos en orden espiral.
 * 
 * Formato de salida:
 * ESPIRAL=<e1> <e2> ... <e_RxC>
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
    // Realiza el recorrido en espiral delimitando los bordes.
    // -----------------------------------------------------------------

    return 0;
}
