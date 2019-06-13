# 6.5 Least Square problem
import numpy as np
import sympy as sp
import linearAlgebra as la 

# 2
A2 = [[2, 1],[-2, 0],[2, 3]]
b2 = [[-5],[8],[1]]
A2T = np.transpose(A2)
A2TA2 = np.dot(A2T, A2)
A2Tb2 = np.dot(A2T, b2)
print('#2')
print(A2TA2)
print(A2Tb2)
A2TA2b2 = np.concatenate((A2TA2, A2Tb2), axis=1)
print(A2TA2b2)
print(sp.Matrix(A2TA2b2).rref())
print()
