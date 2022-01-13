/****Operaciones Aritmeticas****/
//aritmeti.c

#include <stdio.h>

main()
{
    int dato1, dato2, resultado;
    dato1 = 20;
    dato2 = 10;

    //suma
    resultado = dato1 + dato2;
    printf("%d + %d = %d\n", dato1, dato2, resultado);

    //resta
    resultado = dato1 - dato2;
    printf("%d - %d = %d\n", dato1, dato2, resultado);

    //producto
    resultado = dato1 * dato2;
    printf("%d * %d = %d\n", dato1, dato2, resultado);
    
    //conciente
    resultado = dato1 / dato2;
    printf("%d / %d = %d\n", dato1, dato2, resultado);
}
