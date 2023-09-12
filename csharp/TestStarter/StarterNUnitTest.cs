using NUnit.Framework;
using Assert = NUnit.Framework.Assert;

namespace TestStarter;

using NUnit;

[TestFixture]
public class StarterNUnitTest
{
    [Test]
    public void TestSomething()
    {
        Assert.AreEqual(true, false);
    }
}