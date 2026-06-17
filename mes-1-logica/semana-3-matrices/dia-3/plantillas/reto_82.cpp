/*
 * Reto 82: Bubble Sort Optimizado (Conteo de Pasadas)
 * Lee N (1 <= N <= 1000) y N enteros.
 * Implementa Bubble Sort con early termination usando una bandera swapped.
 * Cuenta cuántas pasadas del bucle externo se ejecutan.
 * 
 * Formato de salida:
 * PASADAS=<conteo>
 * ORDENADO=<e1> <e2> ... <eN>
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
    // Implementa burbuja optimizada, cuenta pasadas y muestra la salida.
    // -----------------------------------------------------------------

    return 0;
}
