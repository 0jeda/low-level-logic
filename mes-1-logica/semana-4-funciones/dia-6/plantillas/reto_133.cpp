/*
 * Reto 133: Swap con Punteros
 * Lee A y B.
 * Llama a mi_swap(&A, &B).
 * Imprime A y B.
 *
 * Formato de salida:
 * A=<nuevo_A>
 * B=<nuevo_B>
 */

#include <iostream>

void mi_swap(int* a, int* b) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Intercambia los valores apuntados por a y b.
    // -----------------------------------------------------------------
}

int main() {
    int A, B;
    if (!(std::cin >> A >> B)) return 1;

    mi_swap(&A, &B);

    std::cout << "A=" << A << "\n";
    std::cout << "B=" << B << "\n";

    return 0;
}
