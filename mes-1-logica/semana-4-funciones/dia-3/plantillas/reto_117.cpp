/*
 * Reto 117: Escalar de Arreglo
 * Lee N, luego N enteros, y finalmente factor.
 * Llama a escalarArreglo(arr, N, factor).
 * Imprime el arreglo resultante.
 *
 * Formato de salida:
 * ARR=[x1,x2,...,xn]
 */

#include <iostream>

void escalarArreglo(int arr[], int tam, int factor) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Multiplica cada arr[i] por factor.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    int factor;
    if (!(std::cin >> factor)) return 1;

    escalarArreglo(arr, N, factor);

    std::cout << "ARR=[";
    for (int i = 0; i < N; i++) {
        std::cout << arr[i];
        if (i < N - 1) std::cout << ",";
    }
    std::cout << "]\n";

    return 0;
}
