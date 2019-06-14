// 10) Escribir en C un programa que pida al usuario que ingrese 10 numeros enteros e imprima
// el mınimo, el maximo y el promedio.
#include <stdio.h>

int main(void){

    int i = 0;
    int min = 0;
    int max= 0; 
    int total = 0;
    int num;
    do {
        printf("Ingresar un numero: ");
        scanf("%d", &num);
        if (i == 0 || num < min ) {
            min = num;
        } else if (num > max) {
            max = num;
        }
        total += num;
        i++;
    } while (i < 9);
    printf("min: %i, max: %i, promedio: %i\n", min, max,total / 10);
    return 0;
} 