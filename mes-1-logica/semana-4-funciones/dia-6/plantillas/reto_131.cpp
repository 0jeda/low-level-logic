/*
 * Reto 131: Manipulación Indirecta (Puntero Básico)
 * Lee X.
 * Declara un puntero que apunte a X.
 * Suma 10 a X usando el puntero.
 * Imprime el nuevo valor de X.
 *
 * Formato de salida:
 * VALOR=<nuevo_valor>
 */

#include <iostream>

int main() {
    int X;
    if (!(std::cin >> X)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Declara ptr y suma 10 a X a través de él.
    // -----------------------------------------------------------------

    std::cout << "VALOR=" << X << "\n";

    return 0;
}
