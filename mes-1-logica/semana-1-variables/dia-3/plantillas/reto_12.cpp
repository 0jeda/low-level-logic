/*
 * Reto 12: Clasificador de Caracteres Manual
 * Lee un único carácter C y clasifícalo como:
 * MAYUSCULA, MINUSCULA, DIGITO, u OTRO.
 * 
 * RESTRICCIÓN:
 * No uses <cctype>. Todo debe evaluarse mediante comparaciones de código ASCII.
 */

#include <iostream>

int main() {
    char C;
    // Evitamos omitir espacios por si entra un carácter de espacio u otro
    if (!(std::cin >> std::noskipws >> C)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Clasifica el carácter e imprime MAYUSCULA, MINUSCULA, DIGITO u OTRO.
    // -----------------------------------------------------------------

    return 0;
}
