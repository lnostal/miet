cmake_minimum_required(VERSION 3.11)
set(CONAN_DISABLE_CHECK_COMPILER True)

# проект и версия
project(OpenMP_lab1 CXX)
# поддержкa стандарта С++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_COMPILER /opt/homebrew/Cellar/gcc/13.2.0/bin/g++-13)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -std=c++20 -fopenmp")


# подключение библиотеки pthread для кроссплатформенности //linux
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

# темы
add_executable(without_parallel src/without_parallel.cpp)
add_executable(parallel src/parallel.cpp)


# библиотека для поддержки потоков
target_link_libraries(without_parallel PRIVATE Threads::Threads dl)
target_link_libraries(parallel PRIVATE Threads::Threads dl)



set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
