/*
 * Reto 105: Validador de Tableros Sudoku 9x9
 * Lee una matriz 9x9.
 * Determina si es un tablero de Sudoku válido (sin repetidos de 1-9 en filas, columnas y subcuadrículas 3x3).
 * 
 * Formato de salida:
 * SUDOKU=VALIDO  (si lo es)
 * SUDOKU=INVALIDO (de lo contrario)
 */

#include <iostream>

int main() {
    int tablero[9][9];
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (!(std::cin >> tablero[i][j])) return 1;
        }
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Valida las reglas del Sudoku e imprime VALIDO o INVALIDO.
    // -----------------------------------------------------------------

    return 0;
}
