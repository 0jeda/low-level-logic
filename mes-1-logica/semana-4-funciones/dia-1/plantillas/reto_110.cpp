/*
 * Reto 110: Post-Incremento por Referencia
 * Lee X, S. Llama a postIncrementar(X, S).
 * 
 * Formato de salida:
 * RETORNADO=<valor_anterior>
 * NUEVO=<valor_nuevo>
 */

#include <iostream>

int postIncrementar(int &value, int step) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int X, S;
    if (!(std::cin >> X >> S)) return 1;

    int ret = postIncrementar(X, S);

    std::cout << "RETORNADO=" << ret << "\n";
    std::cout << "NUEVO=" << X << "\n";

    return 0;
}
