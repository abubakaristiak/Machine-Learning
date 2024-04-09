import numpy as np
n1 = np.array([1,2,3,4,5,6,7])
np.save('final_numpy_array',n1)
a = np.load('final_numpy_array.npy')
print(a)