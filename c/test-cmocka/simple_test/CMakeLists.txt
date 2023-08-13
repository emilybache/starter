project(simple-cmocka C)

### The most simple test
add_cmocka_test(simple_test
        SOURCES simple_test.c
        COMPILE_OPTIONS ${DEFAULT_C_COMPILE_FLAGS}
        LINK_OPTIONS ${DEFAULT_LINK_FLAGS}
        LINK_LIBRARIES cmocka-static)
add_cmocka_test_environment(simple_test)
