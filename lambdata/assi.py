from pandas import DataFrame
# related to helper functions
# State abbreviation -> Full Name and visa versa. 
# FL -> Florida, etc. 
# Handle Washington DC and territories like Puerto Rico etc.
def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe
    
    params (my_df) a dataframe with column "abbrev" that has abbreviations
    
    return the copy of original datafram with an additional column
    """
    
    my_df['variable_df'] = my_df.copy()
    df = pd.DataFrame()
    df['df3'] = {"CA": "Cali", "CO": "Colo", "CT": "Conn", "DC": "Wash", "TX": "Tex"}
    my_df["name"] =  df["abbrev"].map(my_df['variable_df'])
    breakpoint()

    return my_df['variable_df']

if __name__ == "__main__":
   
   df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
   print(df.head())

   result_map = add_state_names_column(df)
   print(result_map.head())

   df_data = DataFrame({"one_column": [5,15,20,25,30,35,40,45,50]})
   df_data.head()

   breakpoint()