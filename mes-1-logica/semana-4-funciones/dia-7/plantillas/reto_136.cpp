/*
 * Reto 136: Suma de Matrices (Módulo)
 * Lee F y C, luego matriz A y matriz B.
 * Llama a sumarMatrices(A, B, R, F, C).
 * Imprime R.
 *
 * Formato de salida:
 * FILA_0=[x00,x01,...]
 * ...
 */

#include <iostream>

void sumarMatrices(const int A[][50], const int B[][50], int R[][50], int filas, int columnas) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Suma A y B, guarda en R.
    // -----------------------------------------------------------------
}

int main() {
    int F, C;
    if (!(std::cin >> F >> C)) return 1;

    int A[50][50];
    int B[50][50];
    int R[50][50] = {0};

    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C; j++) {
            if (!(std::cin >> A[i][j])) return 1;
        }
    }

    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C; j++) {
            if (!(std::cin >> B[i][j])) return 1;
        }
    }

    sumarMatrices(A, B, R, F, C);

    for (int i = 0; i < F; i++) {
        std::cout << "FILA_" << i << "=[";
        for (int j = 0; j < C; j++) {
            std::cout << R[i][j];
            if (j < C - 1) std::cout << ",";
        }
        std::cout << "]\n";
    }

    return 0;
}
