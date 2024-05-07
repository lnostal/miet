cmake_minimum_required(VERSION 3.11)

# проект и версия
project(linux_lab2 C CXX)
# поддержкa стандарта С++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/gcc-13)
set(CMAKE_CXX_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/g++-13)

add_executable(lab1 src/lab1.cpp)



set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
