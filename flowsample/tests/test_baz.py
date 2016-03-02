import unittest
from flowsample import baz

class TestBaz(unittest.TestCase):
    def test_baz_returns_baz(self):
        self.assertEquals(baz.baz(), 'baz')
