#include <cgreen/cgreen.h>

Describe(Sample);
BeforeEach(Sample) {}
AfterEach(Sample) {}

Ensure(Sample, test_1) {
    assert_that(1, is_equal_to(4));
}
