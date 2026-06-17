/*
 * Reto 65: Conteo de Elementos Únicos con Offset
 * Lee N (1 <= N <= 1000) y N enteros en el rango [-1000, 1000].
 * Cuenta cuántos elementos únicos existen usando un arreglo con offset.
 * 
 * Formato de salida:
 * UNICOS=<cantidad>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Cuenta elementos únicos aplicando offset para indexar.
    // -----------------------------------------------------------------

    return 0;
}
