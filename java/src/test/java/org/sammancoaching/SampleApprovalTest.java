package org.sammancoaching;

import org.approvaltests.Approvals;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SampleApprovalTest {
    @Test
    void testWithApprovalTests()
    {
        Approvals.verify("Hello World");
    }


    @Test
    void helloWorld() {
        var greetingService = new Greeter();

        var response = greetingService.getGreeting("Emily");

        Approvals.verify(response);
    }
}
