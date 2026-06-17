/*
 * Reto 69: Suma de Tres Elementos (3-Sum)
 * Lee N (3 <= N <= 200) y N enteros desordenados, y una suma objetivo T.
 * Determina si hay tres elementos en posiciones distintas que sumen T.
 * 
 * Formato de salida:
 * PAREJA3=SI  (si existen)
 * PAREJA3=NO  (de lo contrario)
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[200];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int T;
    std::cin >> T;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Ordena el arreglo (O(N^2)) y busca la tripleta que sume T usando dos punteros.
    // -----------------------------------------------------------------

    return 0;
}
