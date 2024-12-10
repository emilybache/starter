<?php

declare(strict_types=1);

namespace Sample\Tests;

use PHPUnit\Framework\TestCase;
use Sample\Sample;

class SampleTest extends TestCase
{
    public function test_something(): void
    {
        $expected = 15;
        $actual = 42;
        self::assertSame($expected, $actual);
    }
}
