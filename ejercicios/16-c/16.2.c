// Ejercicio 16.2. Escribir una función que reciba un número entero n y
// calcule el factorial de n.
// a) En forma iterativa.
// b) En forma recursiva.

#include <stdio.h>

int factorial_iter(int n)
{
    int factorial = 1;
    for (int i = 1; i < n + 1; i++)
    {
        factorial *= i;
    }
    return factorial;
}

int factorial_rec(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return n * factorial_rec(n - 1);
}

int main(void)
{
    printf("%i\n", factorial_iter(5));
    printf("%i\n", factorial_rec(5));
}