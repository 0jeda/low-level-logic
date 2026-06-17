/*
 * Reto 140: Calculadora de Álgebra Lineal Integradora
 * Lee un carácter de operación: '+', '-', '*', o 'T'.
 * 
 * Basado en la operación:
 * - '+' o '-': Lee F C, luego matriz A y matriz B.
 *             Imprime R = A + B o R = A - B.
 * - '*': Lee FA CA, matriz A, luego FB CB, matriz B.
 *         Si CA != FB, imprime "ERROR_DIMENSION" y sale.
 *         Sino, imprime R = A * B.
 * - 'T': Lee N y la matriz cuadrada A de N x N.
 *         Imprime "TRAZA=<resultado>".
 *
 * NOTA: Organiza tu código definiendo las funciones para cada operación
 * y llámalas desde tu bloque de control de flujo.
 */

#include <iostream>

void sumarMatrices(const int A[][50], const int B[][50], int R[][50], int filas, int columnas) {
    // Implementa o copia de retos anteriores
}

void restarMatrices(const int A[][50], const int B[][50], int R[][50], int filas, int columnas) {
    // Implementa o copia de retos anteriores
}

void multiplicarMatrices(const int A[][50], const int B[][50], int R[][50], int filas_A, int cols_A, int cols_B) {
    // Implementa o copia de retos anteriores
}

int calcularTraza(const int A[][50], int n) {
    // Implementa o copia de retos anteriores
}

int main() {
    char op;
    if (!(std::cin >> op)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Implementa el enrutador de comandos y la lectura de matrices.
    // -----------------------------------------------------------------

    return 0;
}
