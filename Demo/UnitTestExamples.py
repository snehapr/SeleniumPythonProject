import unittest
from Examples import Examples


class MyTestCase(unittest.TestCase):
    # setUpclass method will be called once before any test cases are executed
    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    # tearDownClass method will be called once after all the test cases were executed
    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    # setUp method will be called each time before any test case was executed
    def setUp(self):
        print("This will run before for each of the method executed")

    # tearDown method will be called each time after any test case was executed
    def tearDown(self):
        print("This will run after for each of the method executed")

    # Always make sure that the method name should start with 'test' keyword
    # assertEqual method is mainly used to check if the result produces equals the expected one
    def test_add(self):
        result = Examples.add(self, 30, 40)
        self.assertEqual(result, 70)
        # Instead of storing the result of the method in the varible, we can directly call this
        # method in the assertEqual function by passing it as the parameter value
        self.assertEqual(Examples.add(self, 50, 50), 100)
        self.assertEqual((Examples.add(self, -1, 1)), 0)

    def test_sub(self):
        result = Examples.sub(self, 70, 40)
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
