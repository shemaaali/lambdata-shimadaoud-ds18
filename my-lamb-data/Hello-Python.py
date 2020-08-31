from pandas import DataFrame
from myfun import largenum

print("Hello Python")

print(largenum(10))

df = DataFrame({"colors":["red", "white", "blue", "black", "brown", "orange", "yellow", "green", "purple"]})
print(df.head(9))
