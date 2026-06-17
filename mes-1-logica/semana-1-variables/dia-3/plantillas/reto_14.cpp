/*
 * Reto 14: Simulador de Compuertas Lógicas
 * Lee dos enteros A y B (0 o 1) y una cadena OP que representa la operación lógica
 * ("AND", "OR", "XOR", "NAND", "NOR").
 * 
 * Formato de salida:
 * LOGICA=<0 | 1>
 */

#include <iostream>
#include <string>

int main() {
    int A, B;
    std::string OP;
    if (!(std::cin >> A >> B >> OP)) return 1;

    // Convertir a bool
    bool bA = (A != 0);
    bool bB = (B != 0);
    bool resultado = false;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Compara la cadena OP y calcula el valor booleano resultante.
    // -----------------------------------------------------------------

    std::cout << "LOGICA=" << (resultado ? 1 : 0) << "\n";

    return 0;
}
