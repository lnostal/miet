/* Ex5_1.c Печать переменных окружения */
#include <stdio.h>

extern char** environ;

int main () {
    char** var;
    for (var = environ; *var != NULL; ++var)
        printf ("%s\n", *var);
    return 0;
}
