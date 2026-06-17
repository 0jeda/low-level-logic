/*
 * Reto 119: Búsqueda Lineal Modular
 * Lee N, luego N enteros, y finalmente un entero buscado.
 * Llama a buscarElemento(arr, N, buscado) e imprime el índice retornado.
 *
 * Formato de salida:
 * INDICE=<indice>
 */

#include <iostream>

int buscarElemento(const int arr[], int tam, int buscado) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Busca 'buscado' y retorna su índice o -1.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    int buscado;
    if (!(std::cin >> buscado)) return 1;

    std::cout << "INDICE=" << buscarElemento(arr, N, buscado) << "\n";

    return 0;
}
