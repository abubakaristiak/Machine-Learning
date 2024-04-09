import numpy as np
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90,100])

# np.intersect1d(n1,n2)
# only common element:
print(np.intersect1d(n1,n2))
print()

#only unique element:
# np.setdiff1d(n1,n2)  --- unique element in n1
print(np.setdiff1d(n1,n2))


#only unique element:
# np.setdiff1d(n1,n2)  --- unique element in n2
print(np.setdiff1d(n2,n1))