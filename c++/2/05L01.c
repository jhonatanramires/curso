/* 05L01.c Lectura de datos mediante la llaada getc() */

#include <stdio.h>

main()

{
    char ch;
    printf("Escriba, por favor, un carácter:\n");
    ch = getc( stdin );
    printf("El caracter que acaba de introducir es: %c.\n", ch);
    return 0;

}
