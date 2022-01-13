#include <stdio.h>

int multi_enteros( int x, int y )
{
    
    int resultado;
    
    resultado = x * y;
    return resultado;

}

int main()
{

    int _multiplicacion;
    
    _multiplicacion = multi_enteros(3,5);
    printf("La multiplicacion de 3 y 5 es %d.\n", _multiplicacion);
    return 0;

}
