project(sample-cmocka C)

add_cmocka_test(sample_test
        SOURCES sample_test.c
        COMPILE_OPTIONS ${DEFAULT_C_COMPILE_FLAGS}
        LINK_OPTIONS ${DEFAULT_LINK_FLAGS}
        LINK_LIBRARIES src cmocka-static)
add_cmocka_test_environment(add_test)
