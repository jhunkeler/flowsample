import unittest
from flowsample import bar

class TestBar(unittest.TestCase):
    def test_bar_returns_bar(self):
        self.assertEquals(bar.bar(), 'bar')
