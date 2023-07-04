import unittest
from test import min

class TestMyTest(unittest.TestCase):
    
    def test_min1(self):
        val = min(1, 2)
        self.assertEqual(1, val)
    
    def test_min2(self):
        val = min(2, 1)
        self.assertEqual(1, val)
    
    def test_min3(self):
        val = min(-2, -1)
        self.assertEqual(-2, val)
        
if __name__ == "__main__":
    unittest.main()