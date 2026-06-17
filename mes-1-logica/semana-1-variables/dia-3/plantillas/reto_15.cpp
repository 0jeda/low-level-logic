/*
 * Reto 15: Empaquetador de Bits a Byte
 * Lee 8 valores booleanos (0 o 1) representativos de los bits 7 al 0 de un byte.
 * Calcula y muestra el valor entero decimal del byte resultante.
 * 
 * Formato de salida:
 * VALOR=<entero>
 */

#include <iostream>

int main() {
    int bits[8];
    for (int i = 0; i < 8; ++i) {
        if (!(std::cin >> bits[i])) return 1;
    }

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Reconstruye el número decimal sumando la contribución de cada bit
    // según su posición (bits[0] es el Bit 7 (MSB), bits[7] es el Bit 0 (LSB)).
    // -----------------------------------------------------------------

    return 0;
}
