/*
 * Reto 72: Aritmética de Índices 1D
 * Lee R, C, los R x C enteros, y un par de coordenadas (i, j).
 * Muestra el índice lineal (i * C + j) y el valor si es válido, sino ERROR.
 * 
 * Formato de salida:
 * INDICE1D=<indice>
 * VALOR=<valor>
 * (o ERROR si está fuera de rango)
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

    int idx_i, idx_j;
    std::cin >> idx_i >> idx_j;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Verifica límites, calcula el índice 1D e imprime la salida.
    // -----------------------------------------------------------------

    return 0;
}
