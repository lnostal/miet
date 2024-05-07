#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(){

    time_t t;
    int child_pid = fork();

    if (child_pid){
        time(&t);
        printf("Родительский процесс с PID=%d\tPID дочернего процесса=%d\t%s", getpid(), child_pid, ctime(&t));
        sleep(3); 
    } else {
        time(&t);
        printf("Дочерний процесс с PID=%d\tPID родителя=%d\t%s", getpid(), getppid(), ctime(&t));
        sleep(10);
        time(&t);
        printf("\nДочерний процесс после sleep с PID=%d\tPID родителя=%d\t%s", getpid(), getppid(), ctime(&t));
    }
    
    return 0;
}

