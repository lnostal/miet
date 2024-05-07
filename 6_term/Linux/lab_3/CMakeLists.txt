cmake_minimum_required(VERSION 3.11)

# проект и версия
project(linux_lab2 C CXX)
# поддержкa стандарта С++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/gcc-13)
set(CMAKE_CXX_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/g++-13)

add_executable(pr1 src/pr1.c)
add_executable(pr2 src/pr2.c)
add_executable(pr3 src/pr3.c)
add_executable(pr4 src/pr4.c)


set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
