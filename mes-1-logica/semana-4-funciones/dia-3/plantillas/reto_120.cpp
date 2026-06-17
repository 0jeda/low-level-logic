/*
 * Reto 120: Inversión In-Place (En Sitio)
 * Lee N, luego N enteros.
 * Llama a invertirArreglo(arr, N).
 * Imprime el arreglo resultante.
 *
 * Formato de salida:
 * INVERTIDO=[x1,x2,...,xn]
 */

#include <iostream>

void invertirArreglo(int arr[], int tam) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Invierte el arreglo en-sitio (con swaps).
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    invertirArreglo(arr, N);

    std::cout << "INVERTIDO=[";
    for (int i = 0; i < N; i++) {
        std::cout << arr[i];
        if (i < N - 1) std::cout << ",";
    }
    std::cout << "]\n";

    return 0;
}
