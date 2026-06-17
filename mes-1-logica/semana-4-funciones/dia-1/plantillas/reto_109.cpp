/*
 * Reto 109: Limitador de Rango (Clamp por Referencia)
 * Lee X, min_val, max_val. Llama a clamp(X, min_val, max_val).
 * 
 * Formato de salida:
 * CLAMPED=<valor>
 */

#include <iostream>

void clamp(int &val, int min_lim, int max_lim) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int X, min_val, max_val;
    if (!(std::cin >> X >> min_val >> max_val)) return 1;

    clamp(X, min_val, max_val);

    std::cout << "CLAMPED=" << X << "\n";

    return 0;
}
