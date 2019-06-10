// Ejercicio 16.4. Implementar la función unsigned int strlen(const
// char *s) que devuelve la longitud de la cadena s (sin contar el
// último caracter '\0').
// a) En forma iterativa.
// b) En forma recursiva.
#include <stdio.h>

unsigned int _strlen(const char *s)
{
    int length = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        length += 1;
    }
    return length;
}

unsigned int _strlen_iter(const char *s)
{
    printf("%c\n", *s);
    if (*s == 0)
    {
        return 0;
    }
    return 1 + _strlen_iter(s + 1);
}

int main(void)
{
    int len = _strlen_iter("hola mundo!");
    return printf("%i\n", len);
}