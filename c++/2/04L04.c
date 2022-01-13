/* 04L04.c División entera vs. División de punto flotante */
#include <stdio.h>
main()
{
    int int_num1, int_num2, int_num3; /* Declara variables enteras */
    float flt_num1, flt_num2, flt_num3; /* Declara variables de punto flotante */

    int_num1 = 32 / 10;
    int_num2 = 32.0 / 10;
    int_num3 = 32 / 10.0;
    
    flt_num1 = 32 / 10;
    flt_num2 = 32.0 / 10;
    flt_num3 = 32 / 10.0;

    printf("La divión de enteros de 32/10 es: %d\n", int_num1 );
    printf("La divión de punto flotante de 32/10 es: %f\n", flt_num1 );
    printf("La divión de enteros de 32.0/10 es: %d\n", int_num2 );
    printf("La divión de punto flotante de 32.0/10 es: %f\n", flt_num2 );
    printf("La divión de enteros de 32/10.0 es: %d\n", int_num3 );
    printf("La divión de punto flotante de 32/10.0 es: %f\n", flt_num3 );
}
