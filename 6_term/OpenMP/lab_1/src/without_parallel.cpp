
#include <iostream>
#include <chrono>
#include <omp.h>

int main(int argc, char* argv[])
{
   std::setlocale(LC_ALL, "ru_RU");

   if (argc < 3) {
        printf("[usage] script N M\n");
        return 1;
    }

    printf("Размер матрицы %sx%s\n\n", argv[1], argv[2]);

   const int n = atoi(argv[1]);
   const int m = atoi(argv[2]);

    int** matrix = (int**)malloc(sizeof(int*) * n);


    // заполняем массив
    int start_num = 1;
    for (int i = 0; i < n; i++) {
        matrix[i] = (int*)malloc(sizeof(int) * m);

        for (int j = 0; j < m; j++) {
            matrix[i][j] = start_num++;
        }
    }

    std::chrono::steady_clock::time_point start_time = std::chrono::steady_clock::now();

    int i, j, count;

    for (i = 0; i < n; i++) {
        count = 0;        
        for (j = 0; j < m - 1; j++) {
            int num = matrix[i][j] + matrix[i][j + 1];
            while (num) {
                if (num % 10 == 7)
                    count++;
                num /= 10;
            }
        }

        printf("Cтрока %u:\tСемерок: %u\tТредов:%u\n", i + 1, count, omp_get_num_threads());
    }
   
    std::chrono::steady_clock::time_point end_time = std::chrono::steady_clock::now();
    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time);

    printf("\nСкорость выполнения программы: %f\n", time_span.count());

}
