import unittest
from flowsample import foo

class TestFoo(unittest.TestCase):
    def test_foo_returns_foo(self):
        self.assertEquals(foo.foo(), 'foo')
