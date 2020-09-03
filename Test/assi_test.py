# Import a library related to my test called unittest
import unittest
from pandas import DataFrame
from lambdata.assi import add_state_names_column
class TestAssi(unittest.TestCase):

    def test_assi(self):
        
        df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(list(df.columns), ['abbrev'])
        self.assertEqual(df.iloc[3]["abbrev"],'DC')
    
       
        result_map = add_state_names_column(df)

        self.assertEqual(len(result_map.columns), 2)
        self.assertEqual(list(result_map.columns), ['abbrev'])
        self.assertEqual(result_map.iloc[3]["abbrev"], 'DC')
        self.assertEqual(result_map.iloc[3]["name"], 'Washington')
if __name__ == '__main__':
    unittest.main()