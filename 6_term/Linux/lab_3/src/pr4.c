/* Program sharfile.c Usage: progname source_file destination_file
 * for example: sharfile sharfile.c shar.bak */
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/time.h>

int main(int argc,char *argv[])
{

    int             fdrd,fdwt;
    char            c;
    char            parent = 'P';
    char            child ='C'; 
    int             pid;
    unsigned long   i;
    struct timeval  t1, t2, t1_parent, t2_parent;
    double          elapsedTime, elapsedTime_parent;



    if (argc != 3){
        perror("Usage: script [from file] [copy to]\n");
        exit(1);
    }
        
    if ((fdrd = open(argv[1], O_RDONLY)) == -1){
        perror("Error: no such file\n");
        exit(1);
    }

    if ((fdwt = creat(argv[2], 0666)) == -1) {
        perror("Error: disk overflow\n");
        exit(1);
    }

    printf("Parent: creating a child process\n");
    
    pid = fork();

    if (pid == 0) {
        printf("Child process starts, id = %d\n",getpid());
        gettimeofday(&t1, NULL);
        for (;;){
            if (read(fdrd, &c, 1) != 1) 
                break;
            
            for (i=0; i<50000;i++);   /* Long cycle */
            //write(1, &child, 1);
            write(fdwt, &c, 1);
        } 
        gettimeofday(&t2, NULL);
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;
        elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;
        printf("\nChild process time: %f ms.\n", elapsedTime);
        exit(0);

    } else {
        printf("Parent starts, id= %d\n", getpid());
        gettimeofday(&t1_parent, NULL);
        for (;;){
            if (read(fdrd, &c, 1) != 1) 
                break;
            for (i=0;i<50000;i++);  /* Long cycle */
            write(1, &parent, 1);
            write(fdwt, &c, 1);
            }
        gettimeofday(&t2_parent, NULL);
        elapsedTime_parent = (t2_parent.tv_sec - t1_parent.tv_sec) * 1000.0;
        elapsedTime_parent += (t2_parent.tv_usec - t1_parent.tv_usec) / 1000.0;
        printf("\nParent process time: %f ms.\n", elapsedTime_parent);
        wait(0);
    }
}
