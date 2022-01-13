/* 05L01.c Lectura de datos mediante la llaada getc() */

#include <stdio.h>

main()

{
    char ch1, ch2;
    printf("Escriba, por favor, un carácter:\n");
    ch1 = getc( stdin );
    ch2 = getchar(  );
    printf("El primer caracter que acaba de introducir es: %c.\n", ch1);
    printf("El segundo caracter que acaba de introducir es: %c.\n", ch2);
    return 0;

}
