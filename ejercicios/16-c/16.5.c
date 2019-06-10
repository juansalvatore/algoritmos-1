// Ejercicio 16.5. Implementar la función void invertir(char *s)
// que invierte la cadena s (inplace).

#include <stdio.h>
#include <string.h>

void invertir(char *s)
{
    for (int i = 0; i < strlen(s) / 2; i++)
    {
        char prim = *(s + i);
        char ultimo = *(s + strlen(s) - (i + 1));
        *(s + i) = ultimo;
        *(s + strlen(s) - (i + 1)) = prim;
    }
}

int main(void)
{
    char cadena[] = "Hola, Mundo!";
    invertir(cadena);
    return printf("%s\n", cadena);
}