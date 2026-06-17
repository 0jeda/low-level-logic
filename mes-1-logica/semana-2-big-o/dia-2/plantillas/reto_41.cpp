/*
 * Reto 41: Búsqueda de Duplicados (Fuerza Bruta)
 * Lee N y N enteros.
 * Determina si hay elementos duplicados.
 * 
 * Formato de salida:
 * DUPLICADOS=SI  (si hay duplicados)
 * DUPLICADOS=NO  (de lo contrario)
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[1000];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Comprueba duplicados usando bucles anidados.
    // -----------------------------------------------------------------

    return 0;
}
