/*
 * Reto 38: Suma y Promedio Seguro
 * Lee N (0 <= N <= 1000) y N enteros.
 * Calcula la suma y el promedio. Si N = 0, imprime SUMA=0 y PROMEDIO=0.
 * 
 * Formato de salida:
 * SUMA=<suma>
 * PROMEDIO=<promedio>
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
    // Calcula la suma y promedio. Recuerda los decimales del promedio y N=0.
    // -----------------------------------------------------------------

    return 0;
}
