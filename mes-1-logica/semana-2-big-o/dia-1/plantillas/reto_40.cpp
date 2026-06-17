/*
 * Reto 40: Detector de Orden Ascendente
 * Lee N y N enteros.
 * Determina si el arreglo está ordenado de forma ascendente.
 * 
 * Formato de salida:
 * ORDENADO=SI  (si está ordenado)
 * ORDENADO=NO  (de lo contrario)
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
    // Verifica si cada elemento es menor o igual al siguiente e imprime el resultado.
    // -----------------------------------------------------------------

    return 0;
}
