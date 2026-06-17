/*
 * Reto 135: Dirección del Elemento Máximo
 * Lee N y luego N enteros.
 * Llama a buscarMaximo(arr, N) que retorna la dirección del máximo.
 * Calcula el índice restando punteros e imprime la información.
 *
 * Formato de salida:
 * INDICE=<indice>
 * VALOR=<valor_del_maximo>
 */

#include <iostream>

const int* buscarMaximo(const int* arr, int tam) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Retorna un puntero al valor máximo en arr.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> arr[i])) return 1;
    }

    const int* max_ptr = buscarMaximo(arr, N);
    
    // Calcula el índice por aritmética de punteros (max_ptr - arr)
    int indice = max_ptr - arr;

    std::cout << "INDICE=" << indice << "\n";
    std::cout << "VALOR=" << *max_ptr << "\n";

    return 0;
}
