/*
 * Reto 124: Suma de Matrices Modulares
 * Lee F y C, luego la matriz A y finalmente la matriz B.
 * Llama a sumarMatrices(A, B, C, F, C).
 * Imprime la matriz resultante C.
 *
 * Formato de salida:
 * FILA_0=[A00+B00,...]
 * ...
 */

#include <iostream>

void sumarMatrices(const int A[][50], const int B[][50], int C[][50], int filas, int columnas) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Suma A y B, guardando en C.
    // -----------------------------------------------------------------
}

int main() {
    int F, C;
    if (!(std::cin >> F >> C)) return 1;

    int A[50][50];
    int B[50][50];
    int Res[50][50] = {0};

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

    sumarMatrices(A, B, Res, F, C);

    for (int i = 0; i < F; i++) {
        std::cout << "FILA_" << i << "=[";
        for (int j = 0; j < C; j++) {
            std::cout << Res[i][j];
            if (j < C - 1) std::cout << ",";
        }
        std::cout << "]\n";
    }

    return 0;
}
