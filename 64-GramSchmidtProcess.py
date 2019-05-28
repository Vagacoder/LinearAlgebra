# 6.4 The Gram–Schmidt Process
import numpy as np
import sympy as sp
import linearAlgebra as la 

# 13
Q13T = [[5/6, 1/6, -1/2, 1/6],[-1/6, 5/6, 1/6, 1/2]]
A13 = [[5, 9],[1, 7],[-3, -5],[1, 5]]
print('#13')
print(np.dot(Q13T, A13))
print()

# 14
Q14T = [[-2/7, 5/7, 2/7, 4/7],[5/7, 2/7, -4/7, 2/7]]
A14 = [[-2, 3], [5, 7], [2, -2], [4, 6]]
print('#14')
print(np.dot(Q14T, A14))
print()