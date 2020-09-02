from pandas import DataFrame

# related to helper functions
# OOP inherited classes and objects 

class Inherited(DataFrame):
    """
    DataFrame called inherit has th abbrev columns.
    """
    def state_names_column(self):
        """
        Add a column of corresponding state names to a dataframe
        """
        df_state1 = {"AZ": "Arizona", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington", "TX": "Texas", "NE": "Nebraska"}
       
    
        #my_df = self.df_state.copy()
        #self.df_state["names"] = self.df_state["abbrev"].map(df_state1)
        #df_state1 = {"CA": "Cali", "CO": "Colo", "CT": "Conn", "DC": "Wash", "TX": "Tex"}
        #return my_df

        # mutting the copy of dataframe
        self["names"] = self["abbrev"].map(df_state1)

if __name__ == "__main__":
   
   
    inherit = Inherited({"abbrev": ["AZ", "CA", "CO", "CT", "DC", "TX", "NE"]})
    print(inherit.head())
   
    inherit.state_names_column()
    print(inherit.head())
   