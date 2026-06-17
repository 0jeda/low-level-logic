/*
 * Reto 85: K-ésimo Elemento Menor (Burbuja Parcial)
 * Lee N (1 <= N <= 1000) y N enteros, y K (1 <= K <= N).
 * Encuentra el K-ésimo menor elemento mediante un ordenamiento burbuja parcial de K pasos.
 * 
 * Formato de salida:
 * ELEMENTO=<valor>
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
    // Realiza K pasadas de burbuja parcial para colocar el K-ésimo menor e imprímelo.
    // -----------------------------------------------------------------

    return 0;
}
