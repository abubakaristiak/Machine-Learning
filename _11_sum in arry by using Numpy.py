import numpy as np
n1 = np.array([10,20])
n2 = np.array([30,70])

a = np.sum([n1,n2])
print(a)

# axis = 0 it works horizontal element
a1 = np.sum([n1,n2],axis=0)
print(a1)

# axis = 1 it works vertical element
a2 = np.sum([n1,n2],axis=1)
print(a2)
