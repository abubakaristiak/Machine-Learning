import pandas as pd
iris = pd.read_csv('íris.csv')
i1 = iris.head()
i2 = iris.drop('sepal.length',axis=1)
print(i2)