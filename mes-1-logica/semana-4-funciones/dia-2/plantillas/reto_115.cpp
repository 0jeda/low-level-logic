/*
 * Reto 115: Solo Lectura con Referencias Constantes
 * Lee X y F.
 * Llama a calcularFactor(X, F) e imprime el resultado.
 * Las firmas deben forzar parámetros por referencia a constante 'const int &'.
 *
 * Formato de salida:
 * ENTRADA=<num>
 * FACTOR=<factor>
 * RESULTADO=<resultado>
 */

#include <iostream>

int calcularFactor(const int &num, const int &factor) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Retorna la multiplicación de num y factor.
    // -----------------------------------------------------------------
}

int main() {
    int X, F;
    if (!(std::cin >> X >> F)) return 1;

    std::cout << "ENTRADA=" << X << "\n";
    std::cout << "FACTOR=" << F << "\n";
    std::cout << "RESULTADO=" << calcularFactor(X, F) << "\n";

    return 0;
}
