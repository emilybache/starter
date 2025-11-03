import pytest
from approvaltests import verify

from sample import *

def test_something():
    assert True == False

def test_verify():
    verify("Hello World")
