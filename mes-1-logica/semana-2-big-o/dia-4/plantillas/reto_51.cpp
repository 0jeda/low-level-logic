/*
 * Reto 51: Eliminar Duplicados de un Arreglo Ordenado In-Place
 * Lee N (1 <= N <= 1000) y N enteros ordenados.
 * Elimina duplicados compactándolos al inicio en O(N) tiempo y O(1) espacio.
 * 
 * Formato de salida (solo los elementos únicos):
 * ARREGLO=<u1> <u2> ... <uK>
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
    // Elimina duplicados in-place y obtén la nueva longitud lógica K.
    // -----------------------------------------------------------------

    return 0;
}
