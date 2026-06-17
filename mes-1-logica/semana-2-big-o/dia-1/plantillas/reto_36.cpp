/*
 * Reto 36: Simulación de Aritmética de Direcciones
 * Lee N, N enteros, y un índice i.
 * Si i es válido (0 <= i < N), imprime el valor en arr[i] y el offset en bytes.
 * Cada int ocupa 4 bytes.
 * 
 * Formato de salida:
 * VALOR=<valor>
 * OFFSET=<offset_bytes>
 * O simplemente "ERROR" si i es inválido.
 */

#include <iostream>

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    int arr[100];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int idx;
    std::cin >> idx;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Verifica límites e imprime el valor y el offset, o "ERROR".
    // -----------------------------------------------------------------

    return 0;
}
