#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

#define BUF_SIZE 256

int main (int argc, char *argv []) {

    if (argc < 3){
        printf("Usage: script [from file] [copy to]\n");
        return 1;
    }

    int input_fd, output_fd;
    int bytes_in, bytes_out;

    char rec [BUF_SIZE];

    input_fd = open(argv[1], O_RDONLY);
    if (input_fd == -1){
        printf("Error: %s : no such file\n", argv[1]);
        return 2;
    }

    output_fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
    if (output_fd == -1){
        printf("Error: disk overflow\n");
        return 3;
    }

    while ((bytes_in = read(input_fd, rec, BUF_SIZE)) > 0) {
        bytes_out = write(output_fd, rec, bytes_in); 

        if (bytes_in != bytes_out){ 
            printf("Error: file was not copied correctly\n");
            return 4;
        }
    }

    close(input_fd);
    close(output_fd);

    printf("Success!\n");
    return 0;
}

