/*
 * Reto 17: El Intercambio XOR (Bitwise Swap)
 * Lee dos enteros A y B e intercambia sus valores usando XOR.
 * 
 * RESTRICCIÓN:
 * No uses variables auxiliares ni sumas/restas.
 * 
 * Formato de salida:
 * A=<nuevo_A>
 * B=<nuevo_B>
 */

#include <iostream>

int main() {
    int A, B;
    if (!(std::cin >> A >> B)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Realiza el intercambio usando el operador ^ en tres pasos.
    // -----------------------------------------------------------------

    std::cout << "A=" << A << "\n";
    std::cout << "B=" << B << "\n";

    return 0;
}
