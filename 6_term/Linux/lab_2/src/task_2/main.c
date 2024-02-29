#include <stdio.h>
#include "obr.c"

int main()
{
    float x;
    printf("Введите число\n");
    scanf("%f", &x);
    x = obr(x);
    printf("Обратное число: %.3f\n", x);
}