#include <iostream>
#include <omp.h>
#include <chrono>

int main(int argc, char* argv[])
{

	if (argc < 3) {
		printf("[usage] script NMAX LIMIT\n");
		return 1;
	}

	const int NMAX = atoi(argv[1]);
	const int LIMIT = atoi(argv[2]);


	float** matrix = (float**)malloc(sizeof(float*) * NMAX);

	for (int i = 0; i < NMAX; i++) {
		matrix[i] = (float*)malloc(sizeof(float) * NMAX);

		for (int j = 0; j < NMAX; j++) {
			matrix[i][j] = i+j;
		}
	}
	float x = matrix[2][2];

	int i, j;
	float sum;
	int thread_nums = 0;
	std::chrono::steady_clock::time_point start_time = std::chrono::steady_clock::now();

#pragma omp parallel shared(matrix) if (NMAX>LIMIT)
	{
		thread_nums = omp_get_num_threads();

		#pragma omp for private(i,j, sum)
		for (i = 0; i < NMAX; i++) {
			sum = 0;

			for (j = 0; j < NMAX; j++) {
				sum += matrix[i][j];
			}	
		}
	}
	
	std::chrono::steady_clock::time_point end_time = std::chrono::steady_clock::now();
	std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time);

	printf("duration: %f \tthreads: %i\n", time_span.count(), thread_nums);

}