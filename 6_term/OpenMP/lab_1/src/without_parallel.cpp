#include <iostream>
#include <chrono>

int main (int argc, char *argv[])
{
    if (argc < 3) {
        printf("[usage] script N M\n");
        return 1;
    }

    printf("Размер матрицы %sx%s\n\n",argv[1], argv[2]);

    const int n = atoi(argv[1]); 
    const int m = atoi(argv[2]);

    // заполняем массив
    int matrix[n][m];
    int start_num = 1;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            matrix[i][j] = start_num++;
        }
    }

    std::chrono::steady_clock::time_point start_time = std::chrono::steady_clock::now();

    // считаем семерки
    for (int i = 0; i < n; i++){
        int count = 0;
        for (int j = 0; j < m-1; j++){
            int num = matrix[i][j] + matrix[i][j+1];
            while (num){
                if (num%10==7)
                    count++;
                num/=10;
            }
            
        }
        printf ("кол-во семерок в строке %u:\t%u\n",i+1,count);
    }

    std::chrono::steady_clock::time_point end_time = std::chrono::steady_clock::now();
    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time);

    printf("\nСкорость выполнения программы: %f\n",time_span.count());


}