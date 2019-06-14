// 7) Escribir en C una programa que le solicite un numero entero al usuario y muestre por
// pantalla si el numero ingresado es un numero primo o no.
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    n = abs(n);
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            printf("No es primo\n");
            return 0;
        }
    }
    printf("es primo\n");
    return 0;
}
