from pandas import DataFrame
from myfun import largenum
import my-lamb-data

print("Hello Python")

print(largenum(10))

df = DataFrame([[np.nan, 10, 8],
                   [7, np.nan, np.nan],
                   [np.nan, np.nan, np.nan]])

df.head()

my-lamb-data.check_null(df)

dir(my-lamb-data)