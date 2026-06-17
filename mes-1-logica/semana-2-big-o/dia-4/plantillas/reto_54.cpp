/*
 * Reto 54: Rotar Arreglo In-Place (Sin Memoria Auxiliar)
 * Lee N, N enteros, y K.
 * Rota el arreglo a la derecha K posiciones usando O(1) de espacio auxiliar.
 * 
 * Formato de salida:
 * ROTADO=<e1> <e2> ... <eN>
 */

#include <iostream>

// Función auxiliar para invertir un rango del arreglo in-place
void invertir(int arr[], int inicio, int fin) {
    // Implementa tu función de inversión aquí si lo necesitas
}

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
    // Rota el arreglo in-place usando el truco de la triple inversión.
    // -----------------------------------------------------------------

    return 0;
}
