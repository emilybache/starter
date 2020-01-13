cmake_minimum_required(VERSION 3.14..3.16)
set(CMAKE_VERBOSE_MAKEFILE ON)
project(Sample VERSION 1.0
        DESCRIPTION "Sample repo to build code and tests in."
        LANGUAGES CXX)
include(FetchContent)

FetchContent_Declare(
        catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v2.9.2
)
FetchContent_MakeAvailable(catch2)
LIST(APPEND CMAKE_MODULE_PATH
        ${catch2_SOURCE_DIR}/contrib
        )

add_library(catch2 INTERFACE)
target_include_directories(catch2
        INTERFACE ${catch2_SOURCE_DIR}/single_include/catch2
        )

add_executable(sample_catch2
        test/sample_catch.cpp
        test/main.cpp src/sample.h)
set_target_properties(sample_catch2 PROPERTIES CXX_STANDARD 11)
target_include_directories(sample_catch2
        PUBLIC src)
target_link_libraries(sample_catch2 Catch2::Catch2)

include(CTest)
include(ParseAndAddCatchTests)
ParseAndAddCatchTests(sample_catch2)
