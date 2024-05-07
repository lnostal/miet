#include <stdio.h>
#include <stdlib.h>

int main() { 
    
    int ret_val;
    ret_val = system("ls -l /");
    printf("Return code is %d\n", ret_val);
    return ret_val;
}
