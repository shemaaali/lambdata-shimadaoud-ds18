# Do a pytest with assert 
from pandas import DataFrame
from lambdata.assi import add_state_names_column
def test_assii():
        
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})

    assert len(df.columns) == 1
    assert list(df.columns) == ['abbrev']
    assert df.iloc[0]["abbrev"] == 'CA'
        
    
       
    result_map = add_state_names_column(df)

    assert len(result_map.columns) == 1
    assert list(result_map.columns) == ['abbrev', "names"]
    assert result_map.iloc[0]["abbrev"] == 'CA'
    assert result_map.iloc[0]["abbrev"] == 'Cali'