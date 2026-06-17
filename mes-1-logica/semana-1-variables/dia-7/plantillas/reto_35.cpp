/*
 * Reto 35: Simulación de ALU de 1 bit
 * Lee cinco enteros (a, b, cin, op0, op1).
 * Calcula el resultado lógica/aritmético (res) y el acarreo de salida (cout).
 * 
 * Formato de salida:
 * RES=<resultado>
 * COUT=<cout>
 */

#include <iostream>

int main() {
    int a, b, cin, op0, op1;
    if (!(std::cin >> a >> b >> cin >> op0 >> op1)) return 1;

    int res = 0;
    int cout = 0;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Implementa la lógica de selección de operación:
    // op0=0, op1=0 -> AND
    // op0=0, op1=1 -> OR
    // op0=1, op1=0 -> XOR
    // op0=1, op1=1 -> SUMA COMPLETA (Full Adder)
    // -----------------------------------------------------------------

    std::cout << "RES=" << res << "\n";
    std::cout << "COUT=" << cout << "\n";

    return 0;
}
