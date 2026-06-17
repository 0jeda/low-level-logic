/*
 * Reto 108: División y Módulo Simultáneos
 * Lee A y B, y llama a dividir(A, B, cociente, resto).
 * 
 * Formato de salida:
 * COCIENTE=<cociente>
 * RESTO=<resto>
 */

#include <iostream>

void dividir(int dividendo, int divisor, int &cociente, int &resto) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int A, B;
    if (!(std::cin >> A >> B)) return 1;

    int cociente = 0;
    int resto = 0;
    
    dividir(A, B, cociente, resto);

    std::cout << "COCIENTE=" << cociente << "\n";
    std::cout << "RESTO=" << resto << "\n";

    return 0;
}
