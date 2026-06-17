/*
 * Reto 62: El Elemento Único en Parejas (XOR)
 * Lee un entero impar N y N enteros.
 * Todos aparecen dos veces excepto uno. Encuéntralo en O(N) tiempo y O(1) espacio.
 * 
 * Formato de salida:
 * UNICO=<valor>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[999];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Encuentra el elemento único usando XOR.
    // -----------------------------------------------------------------

    return 0;
}
