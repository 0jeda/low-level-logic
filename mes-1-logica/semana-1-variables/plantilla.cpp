/*
 * ============================================================
 *  Reto 1 – El Intercambio de Variables
 *  Archivo : plantilla.cpp
 *  Semana  : 1 – Variables y Tipos de Datos
 *
 *  INSTRUCCIONES:
 *   1. NO modifiques este archivo directamente.
 *   2. Cópialo a  soluciones/<tu_nombre>.cpp  y trabaja allí.
 *   3. Completa el código donde dice  // TU CÓDIGO AQUÍ
 *
 *  RESTRICCIÓN:
 *   - Intercambia A y B usando SÓLO sumas y restas.
 *   - Está PROHIBIDO declarar una tercera variable auxiliar.
 *   - Única librería permitida: <iostream>
 *
 *  FORMATO DE SALIDA ESPERADO (una línea por variable):
 *      A=<valor>
 *      B=<valor>
 * ============================================================
 */

#include <iostream>

int main() {
    int A, B;

    // --- Lectura de datos ---
    std::cin >> A >> B;

    // -------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Intercambia los valores de A y B usando únicamente
    // operaciones aritméticas (+ y -) sobre las mismas dos
    // variables. No puedes declarar ninguna variable extra.
    // -------------------------------------------------------



    // --- Salida de resultados ---
    std::cout << "A=" << A << "\n";
    std::cout << "B=" << B << "\n";

    return 0;
}
