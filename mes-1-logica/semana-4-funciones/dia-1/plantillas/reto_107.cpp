/*
 * Reto 107: Intercambio con Referencias (Swap)
 * Lee A y B, e intercambia sus valores llamando a mi_swap(A, B).
 * 
 * Formato de salida:
 * A=<nuevo_A>
 * B=<nuevo_B>
 */

#include <iostream>

void mi_swap(int &a, int &b) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int A, B;
    if (!(std::cin >> A >> B)) return 1;

    mi_swap(A, B);

    std::cout << "A=" << A << "\n";
    std::cout << "B=" << B << "\n";

    return 0;
}
