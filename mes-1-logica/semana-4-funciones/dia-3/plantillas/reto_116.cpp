/*
 * Reto 116: Sumador de Arreglo
 * Lee N y luego N enteros en un arreglo.
 * Llama a sumarArreglo(arr, N) e imprime el resultado.
 *
 * Formato de salida:
 * SUMA=<resultado>
 */

#include <iostream>

int sumarArreglo(const int arr[], int tam) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Suma todos los elementos y retorna el resultado.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    std::cout << "SUMA=" << sumarArreglo(arr, N) << "\n";

    return 0;
}
