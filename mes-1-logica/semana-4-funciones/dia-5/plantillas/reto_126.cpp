/*
 * Reto 126: Detector de Primos (Puro)
 * Lee N.
 * Llama a esPrimo(N) e imprime 1 si es primo, 0 si no.
 *
 * Formato de salida:
 * PRIMO=<0_o_1>
 */

#include <iostream>

bool esPrimo(int n) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Implementa el test de primalidad puro.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    std::cout << "PRIMO=" << (esPrimo(N) ? 1 : 0) << "\n";

    return 0;
}
