/*
 * Reto 44: Rotar Arreglo a la Derecha
 * Lee N, N enteros, y la cantidad de rotación K.
 * Rota el arreglo a la derecha K posiciones.
 * 
 * Formato de salida:
 * ROTADO=<e1> <e2> ... <eN>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int K;
    std::cin >> K;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Rota el arreglo e imprímelo en el formato indicado.
    // -----------------------------------------------------------------

    return 0;
}
