/*
 * Reto 139: Traza de una Matriz Cuadrada (Módulo)
 * Lee N, luego la matriz de N x N.
 * Llama a calcularTraza(A, N).
 * Imprime la traza resultante.
 *
 * Formato de salida:
 * TRAZA=<resultado>
 */

#include <iostream>

int calcularTraza(const int A[][50], int n) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Suma los elementos de la diagonal principal.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int A[50][50];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!(std::cin >> A[i][j])) return 1;
        }
    }

    std::cout << "TRAZA=" << calcularTraza(A, N) << "\n";

    return 0;
}
