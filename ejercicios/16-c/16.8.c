//  Ejercicio 16.8. Implementar una función que reciba un mensaje y dos números enteros min y
//  max. La función debe pedir al usuario que ingrese un número entero entre min y max (inclusive)
//  y devolverlo. Si el usuario ingresa un valor inválido se le debe informar y pedir que ingrese un
//  nuevo valor, repitiendo hasta que ingrese un número válido.
#include <stdio.h>

int main(void){
    int min= 0;
    int max = 20;
    int valor;
    do {
        printf("Ingresar un numero entero entre %i y %i: ", min, max);
        scanf("%d", &valor);
    } while(valor < min || valor > max);
    printf("Valor: %i\n", valor);
}