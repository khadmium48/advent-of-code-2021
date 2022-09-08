import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
        
# Simple way to run all tests from the command-line interface
if __name__ == '__main__':
    unittest.main()