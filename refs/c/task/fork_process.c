#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int g = 2;

int main() {
    pid_t pid;
    int l = 3;

    printf("PID(%d): Parent g=%d, l=%d \n", getpid(), g, l);
    pid=fork();
    if(pid<0) {
        perror("Fork Error~~!");
        exit(1);
    } else if (pid==0) {
        g ++;
        l ++;
    }
    // 새로이 할당된 프로세스는 주소공간을 포함한 모든 자원들이 새로 할당된다.
    printf("PID(%d):Child g=%d, l=%d \n", getpid(), g, l);
    return 0;
}