cmake_minimum_required(VERSION 3.11)

# проект и версия
project(linux_lab2 C CXX)
# поддержкa стандарта С++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/gcc-13)
set(CMAKE_CXX_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/g++-13)

add_executable(hello src/task_2/hello.cpp)
add_executable(out_err src/task_2/out_err.cpp)
add_executable(obr src/task_2/main.c)

add_executable(ex4_1 src/task_4/ex4_1.c)
add_executable(ex4_2 src/task_4/ex4_2.c)
add_executable(ex4_3 src/task_4/ex4_3.c)

add_executable(ex5_1 src/task_5/ex5_1.c)

add_executable(ex6_1 src/task_6/ex6_1.c)
add_executable(ex6_2 src/task_6/ex6_2.c)


set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
