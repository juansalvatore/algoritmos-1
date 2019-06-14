// 5) Escribir en C una funcion que pida al usuario que ingrese una cadena y la imprima
// invertida.

#include <stdio.h>
#include <string.h>

char invertir_cadena(void)
{
    char palabra[30];
    scanf("%s", palabra);
    int len = 0;
    while (palabra[len] != '\0')
    {
        len++;
    }
    char nueva_palabra[len];
    int j = len - 1;
    int i;
    for (i = 0; i < len; i++)
    {
        nueva_palabra[i] = palabra[j];
        j--;
    }
    nueva_palabra[i] = '\0';
    printf("%s\n", nueva_palabra);
    return 0;
}

int main(void)
{
    invertir_cadena();
    return 0;
}