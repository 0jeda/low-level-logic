/*
 * Reto 93: Suma de Submatriz en Tiempo Constante (Prefix Sum 2D)
 * Lee R, C, y los R x C enteros. Luego Q, y Q consultas de rango (r1 c1 r2 c2).
 * Responde cada consulta en O(1) usando sumas acumuladas en 2D.
 * 
 * Formato de salida:
 * SUMA=<valor>
 */

#include <iostream>

int main() {
    int R, C;
    if (!(std::cin >> R >> C)) return 1;

    int matriz[50][50];
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            std::cin >> matriz[i][j];
        }
    }

    int Q;
    if (!(std::cin >> Q)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Precalcula el arreglo de prefijo 2D de tamaño R x C.
    // Procesa las Q consultas respondiendo en O(1).
    // -----------------------------------------------------------------

    return 0;
}
