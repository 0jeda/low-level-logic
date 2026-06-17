/*
 * Reto 111: Acceso a Variables Sombreadas (Shadowing)
 * Lee un entero X en local que sombrea a la variable global X = 100.
 * Imprime el valor global, el local y la suma.
 * 
 * Formato de salida:
 * GLOBAL=<valor_global>
 * LOCAL=<valor_local>
 * SUMA=<suma>
 */

#include <iostream>

int X = 100;

int main() {
    int X;
    if (!(std::cin >> X)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Usa ::X para acceder a la global y X para la local.
    // -----------------------------------------------------------------

    return 0;
}
