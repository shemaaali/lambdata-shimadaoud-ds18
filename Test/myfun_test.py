# Import a library related to my test called unittest
import unittest
from lambdata.myfun import largenum
class TestMyFun(unittest.TestCase):

    def test_largenum(self):
        self.assertEqual(largenum(10), 900)

if __name__ == '__main__':
    unittest.main()