/*
 * Reto 79: Validador de Matriz Identidad
 * Lee N y la matriz de N x N.
 * Determina si es la matriz identidad.
 * 
 * Formato de salida:
 * IDENTIDAD=SI  (si lo es)
 * IDENTIDAD=NO  (de lo contrario)
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
    // Verifica si cumple ser matriz identidad.
    // -----------------------------------------------------------------

    return 0;
}
