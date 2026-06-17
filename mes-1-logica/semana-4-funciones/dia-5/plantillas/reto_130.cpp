/*
 * Reto 130: Concatenador de Strings Puro
 * Lee dos palabras de std::cin.
 * Llama a concatenar(str1, str2, resultado).
 * Imprime el resultado.
 *
 * Formato de salida:
 * CONCATENADO=<resultado_string>
 */

#include <iostream>

void concatenar(const char str1[], const char str2[], char resultado[]) {
    // -----------------------------------------------------------------
    // TU CÓDIGO AQUÍ: Une str1 y str2 en resultado (ambos estilo C, terminados en '\0').
    // -----------------------------------------------------------------
}

int main() {
    char str1[100];
    char str2[100];
    char resultado[200] = {0};

    if (!(std::cin >> str1 >> str2)) return 1;

    concatenar(str1, str2, resultado);

    std::cout << "CONCATENADO=" << resultado << "\n";

    return 0;
}
