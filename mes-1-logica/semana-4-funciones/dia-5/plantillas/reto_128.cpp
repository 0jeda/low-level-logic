/*
 * Reto 128: Potencia Pura
 * Lee base y exponente.
 * Llama a potencia(base, exponente) e imprime el resultado.
 *
 * Formato de salida:
 * POTENCIA=<resultado>
 */

#include <iostream>

long long potencia(int base, int exponente) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Implementa la potencia pura (exponente >= 0).
    // -----------------------------------------------------------------
}

int main() {
    int B, E;
    if (!(std::cin >> B >> E)) return 1;

    std::cout << "POTENCIA=" << potencia(B, E) << "\n";

    return 0;
}
