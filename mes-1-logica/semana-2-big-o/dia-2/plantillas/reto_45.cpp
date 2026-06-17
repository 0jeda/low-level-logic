/*
 * Reto 45: Suma de Parejas (Suma Objetivo)
 * Lee N, N enteros, y la suma objetivo S.
 * Determina si hay dos elementos distintos que sumen S.
 * 
 * Formato de salida:
 * PAREJA=SI  (si existen)
 * PAREJA=NO  (de lo contrario)
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int S;
    std::cin >> S;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Determina si hay una pareja que sume S.
    // -----------------------------------------------------------------

    return 0;
}
