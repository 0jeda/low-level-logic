/*
 * Reto 132: Recorrido con Punteros (ptr++)
 * Lee N y luego N enteros en un arreglo.
 * Recorre y suma los enteros usando aritmética de punteros (ptr++).
 *
 * Formato de salida:
 * SUMA=<resultado>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    int suma = 0;
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Usa un puntero que avance por el arreglo.
    // -----------------------------------------------------------------

    std::cout << "SUMA=" << suma << "\n";

    return 0;
}
