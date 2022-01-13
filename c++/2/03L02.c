#include <stdio.h>

int suma_enteros( int x, int y )
{
    
    int resultado;
    
    resultado = x + y;
    return resultado;

}

int main()
{

    int _suma;
    
    _suma = suma_enteros(1,12);
    printf("La suma de 1 y 12 es %d.\n", _suma);
    return 0;

}
