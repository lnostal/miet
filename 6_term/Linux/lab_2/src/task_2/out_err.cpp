#include <iostream>
#include <unistd.h>
 /*
 stderr is the standard error message which prints the output 
 message or error message to the console or windows terminal. 
 The stderr is also unlike stdout where stdout prints the output 
 message to the terminal and also can redirect the output message 
 to the file whereas the stderr also prints the output message or 
 error message immediately to the output terminal or console, but 
 it cannot redirect it to the other file.
 */

// ./out_err >> output.txt

int main(int argc, char* argv[])
{

    for (int i = 0;  i < 3; i++){
        fprintf(stdout, "out a\n");
        fprintf(stderr, "err b\n");
        sleep(1);
    }

}