
using NUnit.Framework;
using Verifier = VerifyNUnit.Verifier;

namespace TestStarter;

[TestFixture]
public class StarterVerifyNUnitTest
{
    [Test]
    public Task TestSomething()
    {
        return Verifier.Verify("hello world");
    }
}