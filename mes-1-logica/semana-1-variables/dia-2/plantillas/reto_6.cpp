/*
 * Reto 6: Comparación Flotante Segura
 * Lee tres números double A, B y C. Comprueba si la suma A + B es igual a C
 * usando un margen de error (épsilon) de 1e-6 (0.000001).
 * 
 * Formato de salida:
 * IGUALES   (si la diferencia absoluta es <= 1e-6)
 * DIFERENTES (de lo contrario)
 */

#include <iostream>

int main() {
    double A, B, C;
    if (!(std::cin >> A >> B >> C)) return 1;

    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ
    // Realiza la comparación aproximada con épsilon y muestra el mensaje correspondiente.
    // Pista: Para el valor absoluto a mano, puedes usar una condición simple.
    // -----------------------------------------------------------------

    return 0;
}
