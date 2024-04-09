import pandas as pd
iris = pd.read_csv('iris.csv')

i1 = iris.head()
print(i1)
print()


i2 = iris.tail()
print(i2)
print()


i3 = iris.shape
print(i3)
print()


i4 = iris.describe()
print(i4)


