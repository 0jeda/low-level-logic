/*
 * Reto 106: Duplicador por Valor y Referencia
 * Lee X. Llama a duplicarValor(X) e imprime X.
 * Llama a duplicarReferencia(X) e imprime X.
 * 
 * Formato de salida:
 * VALOR=<valor>
 * REFERENCIA=<valor>
 */

#include <iostream>

void duplicarValor(int x) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

void duplicarReferencia(int &x) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int X;
    if (!(std::cin >> X)) return 1;

    duplicarValor(X);
    std::cout << "VALOR=" << X << "\n";

    duplicarReferencia(X);
    std::cout << "REFERENCIA=" << X << "\n";

    return 0;
}
