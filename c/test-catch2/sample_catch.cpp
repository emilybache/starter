#include "ApprovalTests.hpp"
#include "catch2/catch.hpp"

extern "C"
{
#include "sample.h"
}


TEST_CASE ("Sample") {
    SECTION("sample section") {
        REQUIRE(42 == add(1,2));
    }
}


