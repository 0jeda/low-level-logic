/*
 * Reto 118: Duplicador y Copia de Seguridad
 * Lee N, luego N enteros.
 * Declara un arreglo destino.
 * Llama a copiarArreglo(origen, destino, N).
 * Imprime el arreglo de destino.
 *
 * Formato de salida:
 * DESTINO=[x1,x2,...,xn]
 */

#include <iostream>

void copiarArreglo(const int origen[], int destino[], int tam) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Copia origen a destino.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int origen[1000];
    int destino[1000] = {0}; // Inicializado en 0
    for (int i = 0; i < N; i++) {
        if (!(std::cin >> origen[i])) return 1;
    }

    copiarArreglo(origen, destino, N);

    std::cout << "DESTINO=[";
    for (int i = 0; i < N; i++) {
        std::cout << destino[i];
        if (i < N - 1) std::cout << ",";
    }
    std::cout << "]\n";

    return 0;
}
