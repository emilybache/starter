package codingdojo;

import org.approvaltests.Approvals;
import org.junit.jupiter.api.Test;

public class SampleApprovalTest {
    @Test
    void testWithApprovalTests()
    {
        Approvals.verify("Hello World");
    }
}
