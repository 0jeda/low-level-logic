/*
 * Reto 76: Suma de Diagonales de Matriz Cuadrada
 * Lee N (1 <= N <= 50) y la matriz de N x N.
 * Calcula sumas de las diagonales principal y secundaria y ve si coinciden.
 * 
 * Formato de salida:
 * PRINCIPAL=<suma_principal>
 * SECUNDARIA=<suma_secundaria>
 * IGUALES=<SI | NO>
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
    // Calcula sumas e imprime si coinciden.
    // -----------------------------------------------------------------

    return 0;
}
