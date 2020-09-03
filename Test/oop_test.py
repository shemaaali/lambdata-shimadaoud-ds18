# Import a library related to my test called unittest
import unittest
from pandas import DataFrame
from lambdata.oop import DataCleaner
class TestOOP(unittest.TestCase):

    def test_oop(self):
        
        df_state = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        cleaner = DataCleaner(df_state=df_state)

        self.assertEqual(len(cleaner.df_state.columns), 1)
        self.assertEqual(list(cleaner.df_state.columns), ['abbrev'])
        self.assertEqual(cleaner.df_state.iloc[3]["abbrev"],'DC')
    
    
        cleaner.state_names_column()
    
        self.assertEqual(len(cleaner.df_state.columns), 2)
        self.assertEqual(list(cleaner.df_state.columns), ['abbrev', "names"])
        self.assertEqual(cleaner.df_state.iloc[3]["abbrev"], 'DC')
        self.assertEqual(cleaner.df_state.iloc[3]["names"], 'Washington')
if __name__ == '__main__':
    unittest.main()