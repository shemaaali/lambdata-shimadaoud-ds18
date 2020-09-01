from pandas import DataFrame
from myfun import largenum
from myfun import func_return
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn.metrics import plot_confusion_matrix, classification_report
#from sklearn.metrics import confusion_matrix
#from scipy import stats

DATA_PATH = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Applied-Modeling/master/data/'

# Wrangle data
df = pd.read_csv(DATA_PATH+'apartments/renthop-nyc.csv', 
                 parse_dates=['created'],
                 index_col='created')


# # Split my feature matrix from my target vector
# Target
y=df['price']
X = df[['bathrooms', 'longitude']]

# Use data from April & May 2016 to train
# Use data from June 2016 to test

cutoff2 = '2016-06-1'
mask = X.index < cutoff2

X_train, y_train = X.loc[mask], y.loc[mask]
X_val, y_val = X.loc[~mask], y.loc[~mask]

# plot all the confusion matrixes for models
#fig, ax = plt.subplots(1, 2, figsize=(15, 8))

#sns.heatmap(df,annot=True, fmt="d", cbar=False, cmap="Pastel2",  ax = ax[0]).set_ylim([0,2])
#ax[0].set_title("Confusion Matrix", weight='bold')
#ax[0].set_xlabel('True Labels')
#ax[0].set_ylabel('Actual Labels')

#grades = pd.DataFrame({'good_standing':[True, True, False, False, False, True, True, False, True, True],
                       #'grade_1':['A', 'B', 'A', 'C', 'A', 'A', 'D', 'A', 'B', 'B'],
                       #'grade_2':['Pass', 'Pass', 'Fail', 'Fail', 'Fail','Pass', 'Pass', 'Fail', 'Pass', 'Fail'],
                       #'grade_3':[10, 5, 6, 10, 9, 9, 8, 7, 3, 9]})

#grades.head()

# Contingency Table 
#contingency = pd.crosstab(grades['grade_1'], grades['grade_2'])

#contingency

#chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

#print("chi2 statistic", chi2)
#print("p value", p_value)
#print("degrees of freedom",dof)
#print("expected frequencies table", expected)

table1 = DataFrame(
    [[np.nan, 2],
     [16,    11], 
     [3,      1]],
    index = ['foo','baz', 'zoo'], 
    columns = ['bara', 'barb'])

    # Take the row index, and add it as a new column
table1 = table1.reset_index()

# What is the unique identifier for each row
# Where is the data at that I want to be in my single "tidy" column

tidy = table1.melt(id_vars='index', value_vars=['bara', 'barb'])

tidy

# rename columns
tidy1 = tidy.rename(columns={
    'index': 'name', 
    'variable': 'trt', 
    'value': 'result'
})
tidy1

tidy1.trt = tidy1.trt.str.replace('bar', '')

tidy1

wide = tidy1.pivot_table(index='name', columns='trt', values='result')

wide


df1 = pd.DataFrame({'city':['Omaha', 'Lincoln', 'Columbs', 'Chicago', 'Lesvex','Grandisland', 'Skylar'],
                       'state':['CO', 'CT', 'CA', 'TX', 'NE', 'AI', 'AD'],
                       'zip_code':[68505, 68521, 68506, 68510, 68519, 68501, 68513]


                       })
print(df1.head(10))

print(df.shape)
print(df.head(10))


print("table1:", table1)
print("tidy:", tidy)
print("tidy1:", tidy1)
print("Wide pivot table:", wide)
print("largenum:", largenum(10))
print("Hello Python")
print("largenum:", largenum(10))
print("func_return:", func_return(10, 5))
