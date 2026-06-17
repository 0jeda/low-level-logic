/*
 * Reto 26: Empaquetar 4 Caracteres en un Entero de 32 bits
 * Lee 4 caracteres (C1, C2, C3, C4) y empaquétalos en un unsigned int.
 * 
 * Formato de salida:
 * ENTERO=<valor_decimal>
 */

#include <iostream>

int main() {
    char C1, C2, C3, C4;
    // Evitamos omitir espacios por si entran caracteres vacíos
    if (!(std::cin >> std::noskipws >> C1 >> C2 >> C3 >> C4)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Empaqueta C1 en los bits 31-24, C2 en 23-16, C3 en 15-8, C4 en 7-0.
    // -----------------------------------------------------------------

    return 0;
}
