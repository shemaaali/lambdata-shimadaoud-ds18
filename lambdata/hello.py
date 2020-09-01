from pandas import DataFrame
from myfun import largenum
#from myfun import largenum

print("Hello Python")
print("largenum:", largenum(10))

df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())