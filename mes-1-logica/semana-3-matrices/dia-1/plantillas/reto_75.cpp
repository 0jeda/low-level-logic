/*
 * Reto 75: Comprobar Matriz Simétrica
 * Lee N y los N x N enteros.
 * Determina si la matriz es simétrica.
 * 
 * Formato de salida:
 * SIMETRICA=SI  (si lo es)
 * SIMETRICA=NO  (de lo contrario)
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int matriz[50][50];
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cin >> matriz[i][j];
        }
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Verifica simetría e imprime SI o NO.
    // -----------------------------------------------------------------

    return 0;
}
