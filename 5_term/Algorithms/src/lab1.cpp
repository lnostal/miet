// Лабораторная работа № 1 Методы сортировки
// 5; 19 1000 2800 8500 Метод Хоара

#include <iostream>
#include <vector>
#include <chrono>

// arr - массив для сортировки
// left - стартовый индекс массива
// right - конечный индекс массива
void quick_sort(std::vector<int>& arr, int left, int right) {

    if (left < right) {
        int i = left, j = right; // индексы начала и конца

        int pivot = arr[(left + right) / 2]; // значение на середине

        while (i <= j) {
            // идем слева направо от меньшего до тех пор, 
            // пока значение arr[i] не окажется больше центрального значения 
            while (arr[i] < pivot) {
                i++;
            }
            // идем справа налево от большего до тех пор, 
            // пока значение arr[j] не окажется меньше центрального значения 
            while (arr[j] > pivot) {
                j--;
            }
            
            if (i<=j){
                std::swap(arr[i], arr[j]);
                i++;
                j--;
            }
        }

        quick_sort(arr, left, j);
        quick_sort(arr, i, right);
    }
}

void print_arr(std::vector<int>& arr){
    for (int i = 0; i<arr.size();i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}


void repeat_sort(int n_times, std::vector<int>& default_arr){

    std::cout << "Повторяем сортировку " << n_times << " раз\n";
    std::vector<int> arr;

    for (int i = 0; i<n_times; i++){
        arr = default_arr;
        quick_sort(arr, 0, arr.size()-1);
    }

    print_arr(default_arr);
    print_arr(arr);
}

char* get_time(auto start, auto finish){
    auto time = std::chrono::duration_cast<std::chrono::microseconds>(finish - start).count() / 1000.00;
    char* s_time = new char;
    return std::sprintf(s_time, "%.2lf %s", time, "ms");
}


int main() {

    int N_1 = 1000;
    int N_2 = 2800;
    int N_3 = 8500;

    std::vector<int> default_arr = {-1,39,16,29,4,37,5,-10,-1,6,22,30,37,26,29};

    repeat_sort(N_1, default_arr);
    repeat_sort(N_2, default_arr);
    repeat_sort(N_3, default_arr);

    return 0;
}
