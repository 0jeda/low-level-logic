/*
 * Reto 121: Sumador de Matriz
 * Lee F y C, luego la matriz de F x C.
 * Llama a sumarMatriz(mat, F, C) e imprime el resultado.
 *
 * Formato de salida:
 * SUMA=<resultado>
 */

#include <iostream>

int sumarMatriz(const int mat[][50], int filas, int columnas) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Suma todos los elementos de la matriz.
    // -----------------------------------------------------------------
}

int main() {
    int F, C;
    if (!(std::cin >> F >> C)) return 1;

    int mat[50][50];
    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C; j++) {
            if (!(std::cin >> mat[i][j])) return 1;
        }
    }

    std::cout << "SUMA=" << sumarMatriz(mat, F, C) << "\n";

    return 0;
}
