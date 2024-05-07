#include <stdio.h>
#include <unistd.h>

int main(){

    if (fork()!= 0) {
        execlp("./prog", NULL);
    } 
    return 0;
}

// #include <stdio.h>
// #include <unistd.h>

// int main(){
//     printf("Roses are red\n");
//     sleep(1);
//     printf("Violets are blue\n");
//     sleep(1);
//     printf("TL;DR:\n");
//     sleep(1);
//     printf("They differ in hue.\n");
//     return 0;
// }

