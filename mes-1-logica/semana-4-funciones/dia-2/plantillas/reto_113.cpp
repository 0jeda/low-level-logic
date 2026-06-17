/*
 * Reto 113: Simulación Visual del Call Stack
 * Lee un entero X.
 * Llama a funcionA(X) en main.
 * funcionA llama a funcionB(X - 1).
 * funcionB llama a funcionC(X - 2).
 * Cada una imprime su entrada y salida del stack.
 *
 * Formato de salida:
 * ENTRA_A X=<valor>
 * ENTRA_B X=<valor-1>
 * ENTRA_C X=<valor-2>
 * SALE_C X=<valor-2>
 * SALE_B X=<valor-1>
 * SALE_A X=<valor>
 */

#include <iostream>

void funcionC(int x) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

void funcionB(int x) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Llama a funcionC con x - 1
    // -----------------------------------------------------------------
}

void funcionA(int x) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Llama a funcionB con x - 1
    // -----------------------------------------------------------------
}

int main() {
    int X;
    if (!(std::cin >> X)) return 1;

    funcionA(X);

    return 0;
}
