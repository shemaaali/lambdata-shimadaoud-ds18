import unittest
class TestLambdata(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(True, True )
        self.assertEqual('state'.upper(), 'OtherStatusNames')

    def test_isupper(self):
        self.assertTrue('State'.isupper())
        self.assertFalse('State'.isupper())

    def test_split(self):
        ttest1 = 'TestSuccess TestCompleted '
        self.assertEqual(ttest1 .split(), ['TestSuccess', 'TestCompleted'])

        # Let's check ttest1 to see if the split fails or not
        with self.assertRaises(TypeError):
            ttest1.split(2)

if __name__ == '__main__':
    unittest.main()