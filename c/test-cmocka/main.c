#include <stdarg.h>
#include <setjmp.h>
#include <stddef.h>
#include "cmocka.h"

#include "sample.h"

static void test_add(void **state)
{
    assert_int_equal(2, 8);
}

int main() {
    const struct CMUnitTest tests[] =
            {
                    cmocka_unit_test(test_add),
            };

    return cmocka_run_group_tests(tests, NULL, NULL);
}