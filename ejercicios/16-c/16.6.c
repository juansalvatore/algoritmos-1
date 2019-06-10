// Ejercicio 16.6. Implementar la función void strcpy(const char *origen, char *destino) que
// copia la cadena origen en la dirección de memoria apuntada por destino. Asumir que destino
// apunta a un arreglo de caracteres con espacio suficiente (strlen(origen) + 1).
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void _strcpy(const char *origen, char *destino)
{
    char act = *(origen);
    int i = 0;
    while (act)
    {

        act = *(origen + i);
        *(destino + i) = act;
        i++;
    }
    *(destino + strlen(origen)) = '\0';
}

int main(void)
{
    char *str;
    int size = 4;
    str = (char *)malloc(sizeof(char) * size);
    _strcpy("abc", str);
    printf("%s\n", str);
    return 0;
}