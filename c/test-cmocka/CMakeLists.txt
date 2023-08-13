set(TEST_NAME test-cmocka)
set(SOURCE_FILES main.c)
include(FetchContent)

FetchContent_Declare(
        cmocka
        GIT_REPOSITORY https://git.cryptomilk.org/projects/cmocka.git
        GIT_TAG        cmocka-1.1.5
        GIT_SHALLOW    1
)

set(WITH_STATIC_LIB ON CACHE BOOL "CMocka: Build with a static library" FORCE)
set(WITH_CMOCKERY_SUPPORT OFF CACHE BOOL "CMocka: Install a cmockery header" FORCE)
set(WITH_EXAMPLES OFF CACHE BOOL "CMocka: Build examples" FORCE)
set(UNIT_TESTING OFF CACHE BOOL "CMocka: Build with unit testing" FORCE)
set(PICKY_DEVELOPER OFF CACHE BOOL "CMocka: Build with picky developer flags" FORCE)

FetchContent_MakeAvailable(cmocka)

add_executable(${TEST_NAME} main.c)
target_sources(${TEST_NAME} PRIVATE ${SOURCE_FILES})
target_compile_features(${TEST_NAME} PRIVATE c_std_99)
target_link_libraries(${TEST_NAME} PRIVATE src cmocka-static)

enable_testing()
#add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME})
