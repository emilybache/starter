#include <cgreen/cgreen.h>
#include "sample.c"

TestSuite *sample_tests() {
    TestSuite *suite = create_test_suite();
    add_test_with_context(suite, Sample, test_1);
    return suite;
}

int main(int argc, char **argv) {
    TestSuite *suite = create_test_suite();
    add_suite(suite, sample_tests());
    if (argc > 1) {
        return run_single_test(suite, argv[1], create_text_reporter());
    }
    return run_test_suite(suite, create_text_reporter());
}
