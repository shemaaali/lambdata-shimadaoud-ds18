from pandas import DataFrame
from lambdata.myfun import largenum

print("Hello Python")
print("largenum:", largenum(9))

df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())