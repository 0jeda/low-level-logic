/*
 * Reto 129: Filtrado Inmutable de Pares
 * Lee N, luego N enteros.
 * Declara un arreglo destino.
 * Llama a filtrarPares(origen, N, destino) que retorna la cantidad de pares.
 * Imprime el arreglo de destino.
 *
 * Formato de salida:
 * PARES=[x1,x2,...,xm]
 */

#include <iostream>

int filtrarPares(const int origen[], int tam, int destino[]) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Filtra los pares de origen a destino. Retorna la cantidad.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int origen[1000];
    int destino[1000] = {0};

    for (int i = 0; i < N; i++) {
        if (!(std::cin >> origen[i])) return 1;
    }

    int total_pares = filtrarPares(origen, N, destino);

    std::cout << "PARES=[";
    for (int i = 0; i < total_pares; i++) {
        std::cout << destino[i];
        if (i < total_pares - 1) std::cout << ",";
    }
    std::cout << "]\n";

    return 0;
}
