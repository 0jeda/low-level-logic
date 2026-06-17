/*
 * Reto 58: Consultas Rápidas de Suma en Rango (Prefix Sum)
 * Lee N, N enteros, Q, y Q consultas (L y R).
 * Responde cada consulta en O(1) usando sumas acumuladas precalculadas en O(N).
 * 
 * Formato de salida (una línea por consulta):
 * SUMA=<valor>
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int Q;
    if (!(std::cin >> Q)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Precalcula el arreglo de sumas acumuladas (prefijo) de tamaño N.
    // Procesa las Q consultas respondiendo en O(1) cada una.
    // -----------------------------------------------------------------

    return 0;
}
