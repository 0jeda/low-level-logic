/*
 * Reto 112: Contador de Visitas Estático
 * Lee N (número de pasos) y luego N enteros.
 * Llama a registrarPaso(val) con cada entero.
 *
 * Cada llamada debe usar variables 'static' internas en registrarPaso
 * para contar cuántas veces ha sido llamada la función y acumular el valor.
 *
 * Formato de salida por cada llamada:
 * LLAMADA=<numero> SUMA=<acumulado>
 */

#include <iostream>

void registrarPaso(int valor) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Declara variables static y realiza el acumulado.
    // -----------------------------------------------------------------
}

int main() {
    int N;
    if (!(std::cin >> N)) return 1;

    for (int i = 0; i < N; i++) {
        int val;
        if (std::cin >> val) {
            registrarPaso(val);
        }
    }
    return 0;
}
