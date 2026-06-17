/*
 * Reto 114: Detector y Prevención de Stack Overflow
 * Lee N y MAX_DEPTH.
 * Llama a recursiva(N, 1, MAX_DEPTH).
 *
 * En cada llamada recursiva:
 * 1. Si el depth actual es estrictamente mayor que max_depth,
 *    imprime "STACK_OVERFLOW_PREVENIDO depth=<depth>" y termina la recursión.
 * 2. Si no, imprime "DEPTH=<depth> VALOR=<n>"
 * 3. Si n == 0, imprime "FIN n=0" y termina.
 * 4. Si no, realiza la llamada recursiva decrementando n e incrementando depth.
 */

#include <iostream>

void recursiva(int n, int depth, int max_depth) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // -----------------------------------------------------------------
}

int main() {
    int N, MAX_DEPTH;
    if (!(std::cin >> N >> MAX_DEPTH)) return 1;

    recursiva(N, 1, MAX_DEPTH);

    return 0;
}
