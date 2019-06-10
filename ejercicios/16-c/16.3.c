// Ejercicio 16.3. Escribir una función que reciba un arreglo de números
// y la cantidad de elementos, y devuelva el promedio

#include <stdio.h>

float promedio(float array[], int n)
{
    float total = 0;
    for (int i = 0; i < n; i++)
    {
        total += array[i];
    }
    return total / n;
}

int main(void)
{
    float array[] = {5, 5, 5, 4, 5};
    printf("%.2f\n", promedio(array, 5));
}