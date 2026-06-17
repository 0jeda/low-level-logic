/*
 * Reto 1: El Intercambio de Variables
 * Escribe un programa que lea dos enteros A y B, e intercambie sus valores
 * usando únicamente sumas y restas sobre A y B.
 * Está estrictamente prohibido declarar variables auxiliares.
 */

#include <iostream>

int main() {
    int A, B;
    
    // Leer valores
    if (!(std::cin >> A >> B)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Intercambia los valores de A y B usando sólo sumas y restas.
    // -----------------------------------------------------------------

    // Imprimir resultados
    std::cout << "A=" << A << "\n";
    std::cout << "B=" << B << "\n";

    return 0;
}
