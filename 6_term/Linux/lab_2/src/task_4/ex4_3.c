/* Ex4_3.c Печать произвольного числа параметров */
#include  <stdio.h>

int main(int argc, char *argv[]) {
    for  (; *argv; ++argv){
        int x = atoi(*argv);
 		printf("type of int argv %i\n", x);
    }
}