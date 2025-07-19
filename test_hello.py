import unittest
from hello import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("DevOps"), "Hello, DevOps!")

if __name__ == "__main__":
    unittest.main()
