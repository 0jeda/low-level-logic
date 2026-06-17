/*
 * Reto 59: Detector de Subarreglo con Suma Cero
 * Lee N (1 <= N <= 100) y N enteros.
 * Determina si hay algún subarreglo continuo que sume exactamente 0.
 * 
 * Formato de salida:
 * SUMA_CERO=SI  (si existe)
 * SUMA_CERO=NO  (de lo contrario)
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[100];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Comprueba si existe algún subarreglo que sume 0.
    // -----------------------------------------------------------------

    return 0;
}
