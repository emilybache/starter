﻿using System;
using System.Collections.Generic;
using System.Text;
using Xunit;
using Assert = Xunit.Assert;

namespace TestStarter;

public class StarterXUnitTest
{
    [Fact]
    public void TestSomething()
    {
        Assert.Equal(true, false);
    }
}