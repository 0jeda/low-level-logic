/*
 * Reto 123: Transposición de Matrices
 * Lee F y C, luego la matriz de F x C.
 * Declara una matriz destino de 50x50.
 * Llama a transponerMatriz(origen, F, C, destino).
 * Imprime la matriz de destino usando el formato FILA_i=[...]
 * NOTA: La matriz transpuesta tiene C filas y F columnas.
 */

#include <iostream>

void transponerMatriz(const int origen[][50], int filas, int columnas, int destino[][50]) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Realiza la transpuesta en destino.
    // -----------------------------------------------------------------
}

int main() {
    int F, C;
    if (!(std::cin >> F >> C)) return 1;

    int origen[50][50];
    int destino[50][50] = {0};

    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C; j++) {
            if (!(std::cin >> origen[i][j])) return 1;
        }
    }

    transponerMatriz(origen, F, C, destino);

    // Imprimir la matriz transpuesta (filas = C, columnas = F)
    for (int i = 0; i < C; i++) {
        std::cout << "FILA_" << i << "=[";
        for (int j = 0; j < F; j++) {
            std::cout << destino[i][j];
            if (j < F - 1) std::cout << ",";
        }
        std::cout << "]\n";
    }

    return 0;
}
