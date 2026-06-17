/*
 * Reto 94: Multiplicación de Matriz por Vector
 * Lee R, C, los R x C enteros de la matriz, y el vector de tamaño C.
 * Realiza el producto y muestra el vector resultante de tamaño R.
 * 
 * Formato de salida:
 * VECTOR=<v1> <v2> ... <vR>
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

    int vec[50];
    for (int j = 0; j < C; ++j) {
        std::cin >> vec[j];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Realiza el producto M x V e imprime el vector resultante.
    // -----------------------------------------------------------------

    return 0;
}
