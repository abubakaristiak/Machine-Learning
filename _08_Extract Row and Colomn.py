import pandas as pd

# Assuming 'iris.csv' file is in the same directory
iris = pd.read_csv('iris.csv')

# Display the first 5 rows using head()
i1 = iris.head()
print(i1)

# iloc method to select specific rows and columns using integer indices
i2 = iris.iloc[0:5, 0:3]
print(i2)

# loc method to select rows 5 to 11 and columns 'petal.length' and 'variety'
i3 = iris.loc[5:11, ['petal.length', 'variety']]
print(i3)
