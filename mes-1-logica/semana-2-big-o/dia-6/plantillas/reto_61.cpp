/*
 * Reto 61: Conteo de Frecuencias en Rango [0, 9]
 * Lee N (1 <= N <= 1000) y N enteros en el rango [0, 9].
 * Muestra la frecuencia de los números presentes.
 * 
 * Formato de salida:
 * <número>:<frecuencia>
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
    // Cuenta y muestra las frecuencias usando un arreglo de tamaño 10.
    // -----------------------------------------------------------------

    return 0;
}
