/*
 * Reto 73: Matriz Transpuesta
 * Lee R, C, y los R x C enteros.
 * Genera e imprime la transpuesta de tamaño C x R.
 * 
 * Formato de salida:
 * TRANSPUESTA=
 * <elementos fila 0 de la transpuesta separados por espacio>
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
    // Calcula la transpuesta e imprímela.
    // -----------------------------------------------------------------

    return 0;
}
