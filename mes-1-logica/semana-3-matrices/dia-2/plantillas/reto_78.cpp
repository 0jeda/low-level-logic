/*
 * Reto 78: Rotar Matriz 90 Grados a la Derecha In-Place
 * Lee N (1 <= N <= 50) y la matriz N x N.
 * Rota la matriz 90 grados a la derecha (sentido horario) in-place.
 * 
 * RESTRICCIÓN:
 * No utilices una segunda matriz auxiliar.
 * 
 * Formato de salida:
 * ROTADA=
 * <elementos fila 0 rotados separados por espacio>
 * ...
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
    // Rota la matriz in-place mediante transposición e inversión de filas.
    // -----------------------------------------------------------------

    return 0;
}
