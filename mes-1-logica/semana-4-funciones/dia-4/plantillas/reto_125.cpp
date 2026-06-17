/*
 * Reto 125: Copia Segura de Matrices
 * Lee F y C, luego la matriz.
 * Llama a copiarMatriz(origen, destino, F, C).
 * Imprime la matriz destino.
 *
 * Formato de salida:
 * FILA_0=[x00,...]
 * ...
 */

#include <iostream>

void copiarMatriz(const int origen[][50], int destino[][50], int filas, int columnas) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Copia origen a destino.
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

    copiarMatriz(origen, destino, F, C);

    for (int i = 0; i < F; i++) {
        std::cout << "FILA_" << i << "=[";
        for (int j = 0; j < C; j++) {
            std::cout << destino[i][j];
            if (j < C - 1) std::cout << ",";
        }
        std::cout << "]\n";
    }

    return 0;
}
