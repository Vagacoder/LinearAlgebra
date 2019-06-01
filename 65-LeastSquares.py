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

# 4
A4 = [[1, 3],[1, -1],[1, 1]]
b4 = [[5],[1],[0]]
A4T = np.transpose(A4)
A4TA4 = np.dot(A4T, A4)
A4Tb4 = np.dot(A4T, b4)
print('#4')
print(A4TA4)
print(A4Tb4)
A4TA4b4 = np.concatenate((A4TA4, A4Tb4), axis=1)
print(A4TA4b4)
print(sp.Matrix(A4TA4b4).rref())
print()

# 12
ATAb12 = [[3, 2, -2, 13],[2, 3, 0, 14],[-2, 0, 3, -5]]
print('#12')
print(sp.Matrix(ATAb12).rref())
print()
