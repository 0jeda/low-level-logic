/*
 * Reto 122: Visualizador de Matriz Formateada
 * Lee F y C, luego la matriz de F x C.
 * Llama a imprimirMatriz(mat, F, C).
 *
 * Formato de salida:
 * FILA_0=[x00,x01,...,x0n]
 * FILA_1=[x10,x11,...,x1n]
 * ...
 */

#include <iostream>

void imprimirMatriz(const int mat[][50], int filas, int columnas) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Imprime cada fila en el formato indicado.
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

    imprimirMatriz(mat, F, C);

    return 0;
}
