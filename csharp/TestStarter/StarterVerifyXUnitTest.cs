using Verifier = VerifyXunit.Verifier;

namespace TestStarter;

[UsesVerify]
public class StarterVerifyXUnitTest
{
    [Fact]
    public Task TestSomething()
    {
        return Verifier.Verify("hello world");
    }
}