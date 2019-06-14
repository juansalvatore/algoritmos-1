// Escribir en C un programa que pida al usuario dos palabras. El programa debe impri-
// mir ambas palabras en una lınea, separadas por una secuencia de puntos de forma tal que la

// longitud total de la lınea sea de 30 caracteres. Ejemplo:
// Primera palabra: Hola
// Segunda palabra: Mundo
// Hola.....................Mundo
// hola.................mundo
// hola.....................mundo
#include <stdio.h>

int length(char *string)
{
    int count = 0;
    while (string[count] != '\0')
        count++;
    return count;
}

int main(void)
{
    char palabra1[15], palabra2[15], palabra_final[31];
    int MAX = 30;
    static int i=0;
    int j=0;
    int k=0;
    printf("Primera palabra: ");
    scanf("%s", palabra1);
    printf("Segunda palabra: ");
    scanf("%s", palabra2);

    int len_palabra1 = length(palabra1);
    int len_palabra2 = length(palabra2);

    while(palabra1[i]!='\0')
    {
        palabra_final[i] = palabra1[i];
        i++;
    }
    while(j < (30 - len_palabra2 - len_palabra1))
    {
        palabra_final[i]='.';
        j++;
        i++;
    }
    while(palabra2[k]!='\0')
    {
        palabra_final[i]=palabra2[k];
        i++;
        k++;
    }
    palabra_final[i]='\0';
    // for (int j = len_palabra1; j < 31; j++)
    // {
    //     palabra_final[j] = '.';
    // }
    // int count = 0; 
    // for (int k = length(palabra_final) - len_palabra2; k < 31; k++)
    // {
    //     palabra_final[k] = palabra2[count];
    //     count++;
    // }
    printf("%s\n", palabra_final);
    return 0;
}
