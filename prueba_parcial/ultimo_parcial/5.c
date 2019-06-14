// 6) Escribir en C un programa que pida al usuario un valor mınimo, un valor maximo y un
// numero n, e imprima una tabla con los cuadrados de los numeros entre mınimo y maximo cada
// n numeros. Por ejemplo (mınimo = 0, maximo = 17, n = 5) debe mostrar:
// 0 0
// 5 25
// 10 100
// 15 225
#include <stdio.h>

int main(void)
{
    int min, max, n;
    scanf("%d", &min);
    scanf("%d", &max);
    scanf("%d", &n);

    for (int i = min; i < max; i = i + n)
    {
        printf("%i %i\n", i, i * i);
    }
    return 0;
}