/*
 * Reto 138: Multiplicación de Matrices (Módulo)
 * Lee F_A y C_A, luego matriz A.
 * Lee F_B y C_B, luego matriz B.
 * Llama a multiplicarMatrices(A, B, R, F_A, C_A, C_B).
 * Imprime R.
 *
 * Formato de salida:
 * FILA_0=[x00,x01,...] (de F_A filas y C_B columnas)
 * ...
 */

#include <iostream>

void multiplicarMatrices(const int A[][50], const int B[][50], int R[][50], int filas_A, int cols_A, int cols_B) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Realiza la multiplicación de A y B (A * B), guarda en R.
    // Recuerda inicializar R en 0 si no se hizo en main o limpiarlo antes.
    // -----------------------------------------------------------------
}

int main() {
    int FA, CA;
    if (!(std::cin >> FA >> CA)) return 1;

    int A[50][50];
    for (int i = 0; i < FA; i++) {
        for (int j = 0; j < CA; j++) {
            if (!(std::cin >> A[i][j])) return 1;
        }
    }

    int FB, CB;
    if (!(std::cin >> FB >> CB)) return 1;

    int B[50][50];
    for (int i = 0; i < FB; i++) {
        for (int j = 0; j < CB; j++) {
            if (!(std::cin >> B[i][j])) return 1;
        }
    }

    int R[50][50] = {0};

    multiplicarMatrices(A, B, R, FA, CA, CB);

    for (int i = 0; i < FA; i++) {
        std::cout << "FILA_" << i << "=[";
        for (int j = 0; j < CB; j++) {
            std::cout << R[i][j];
            if (j < CB - 1) std::cout << ",";
        }
        std::cout << "]\n";
    }

    return 0;
}
