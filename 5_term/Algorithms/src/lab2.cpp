// Лабораторная работа № 2 Методы поиска
//  5; 18 Поиск по бинарному дереву

// 5; 18 1000 2800 8500

#include <iostream>
#include <vector>

int binarySearch(std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // Возвращаем -1, если элемент не найден
}

int main() {
    std::vector<int> arr = {2, 4, 6, 8, 10, 12, 14, 16, 18};
    int target = 10;

    int index = binarySearch(arr, target);

    if (index != -1) {
        std::cout << "Element found at index: " << index << std::endl;
    } else {
        std::cout << "Element not found in the array." << std::endl;
    }

    return 0;
}
