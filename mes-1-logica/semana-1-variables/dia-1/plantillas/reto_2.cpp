/*
 * Reto 2: Suma Segura
 * Lee dos enteros con signo de 32 bits (A y B) y determina si su suma
 * causará un desbordamiento por exceso (OVERFLOW) o por defecto (UNDERFLOW).
 * Si la suma es segura, imprime el resultado de la suma.
 * 
 * RESTRICCIÓN:
 * No puedes usar variables de mayor tamaño (como long long) para validar.
 * Debes calcularlo usando lógica con los mismos tipos 'int'.
 */

#include <iostream>
// Puedes usar <limits> para obtener los valores máximos y mínimos de int.
#include <limits>

int main() {
    int A, B;
    if (!(std::cin >> A >> B)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Detecta overflow/underflow antes de realizar la suma.
    // Pistas: 
    //   std::numeric_limits<int>::max() nos da el entero máximo.
    //   std::numeric_limits<int>::min() nos da el entero mínimo.
    // -----------------------------------------------------------------

    return 0;
}
