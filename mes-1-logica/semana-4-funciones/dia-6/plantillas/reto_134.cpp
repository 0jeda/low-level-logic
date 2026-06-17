/*
 * Reto 134: Prueba Empírica del Decay
 * Declara 'int arr[10];' en main.
 * Llama a obtenerTamanoDecay(arr).
 * Imprime el sizeof medido localmente en main, y el retornado por la función.
 *
 * Formato de salida:
 * LOCAL_SIZE=40
 * DECAYED_SIZE=<tamano_de_un_puntero>
 */

#include <iostream>

int obtenerTamanoDecay(int arr[]) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Retorna el sizeof de arr en este contexto.
    // -----------------------------------------------------------------
}

int main() {
    int arr[10];
    
    std::cout << "LOCAL_SIZE=" << sizeof(arr) << "\n";
    std::cout << "DECAYED_SIZE=" << obtenerTamanoDecay(arr) << "\n";

    return 0;
}
