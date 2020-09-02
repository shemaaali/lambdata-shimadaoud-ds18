from pandas import DataFrame

# related to helper functions
# OOP classes and objects 

class DataCleaner():
    def __init__(self, df_state):
        """
        params (df_state) a dataframe with column "abbrev" that has abbreviations
        """
        self.df_state = df_state

    def state_names_column(self):
        """
        Add a column of corresponding state names to a dataframe

        return the copy of original datafram with an additional column
        """
        df_state1 = {"AZ": "Arizona", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington", "TX": "Texas", "NE": "Nebraska"}
       
    
        #my_df = self.df_state.copy()
        #self.df_state["names"] = self.df_state["abbrev"].map(df_state1)
        #df_state1 = {"CA": "Cali", "CO": "Colo", "CT": "Conn", "DC": "Wash", "TX": "Tex"}
        #return my_df

        # mutting the copy of dataframe
        self.df_state["names"] = self.df_state["abbrev"].map(df_state1)

if __name__ == "__main__":
   
   df_state = DataFrame({"abbrev": ["AZ", "CA", "CO", "CT", "DC", "TX", "NE"]})
 
   cleaner = DataCleaner(df_state=df_state)
   print(cleaner.df_state.head(7))
   cleaner.state_names_column()
   print(cleaner.df_state.head(7))