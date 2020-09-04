# Do test large number with pytest
from lambdata.myfun import largenum

def test_largenum():
     assert largenum(9) == 900