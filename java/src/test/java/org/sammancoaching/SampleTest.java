package org.sammancoaching;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SampleTest {
    @Test
    void sample() {
        assertEquals(true, false);
    }

    @Test
    void helloWorld() {
        var greetingService = new Greeter();

        var response = greetingService.getGreeting("Emily");

        assertEquals("Hello, Emily!", response);
    }
}
