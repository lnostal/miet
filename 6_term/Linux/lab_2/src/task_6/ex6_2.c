#include <stdio.h>
#include <time.h>

#define FILE_NAME "file1"

int main (int argc, char *argv []) {

    time_t t = time(NULL);
    char* time_str = asctime(localtime(&t));
    printf("local:     %s", time_str);

    FILE *file = fopen(FILE_NAME, "a");

    int results = fputs(time_str, file);
    if (results == EOF) {
        return 4;
    }

    fclose(file);
}