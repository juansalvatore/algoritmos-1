// Ejercicio 16.1. Escribir una función que permita calcular el área de un rectángulo dada su base
// y altura.
#include <stdio.h>

int area_rectangulo(float base, float altura)
{
    return base * altura;
}

int main(void)
{
    float area = area_rectangulo(2, 2);
    printf("%.1f\n", area);
}