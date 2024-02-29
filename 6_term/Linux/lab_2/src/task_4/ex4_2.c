/* Ex4_2.c Печать произвольного числа параметров */
#include  <stdio.h>

int main(int argc, char *argv[]) {
    for  (; *argv; ++argv)
        printf("%s\n", *argv);
}
