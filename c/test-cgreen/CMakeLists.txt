set(TEST_NAME sample_test_cgreen)
set(SOURCE_FILES main.c)
enable_testing()
find_package(cgreen)

add_executable(${TEST_NAME})
target_sources(${TEST_NAME} PRIVATE ${SOURCE_FILES})
target_link_libraries(${TEST_NAME} src cgreen)
add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME})
