cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(Sample VERSION 1.0)

set(CMAKE_C_STANDARD 11)

add_subdirectory(src)
add_subdirectory(test-cmocka)
add_subdirectory(test-catch2)
add_subdirectory(test-cgreen)
add_subdirectory(test-gtest)
