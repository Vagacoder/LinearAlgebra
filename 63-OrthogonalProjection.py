# 6.3 Orthogonal Projections
import numpy as np
import sympy as sp
import linearAlgebra as la 

# 6 
y6 = [[6],[4],[1]]
u61 = [[-4],[-1],[1]]
u62 = [[0],[1],[1]]
a6 = [[-4, 0, 6],[-1, 1, 4],[1, 1, 1]]
print('#6')
print(sp.Matrix(a6).rref())
print()

# 17
UUT17 = [[8/9, -2/9, 2/9],[-2/9, 5/9, 4/9],[2/9, 4/9, 5/9]]
y17 = [[4],[8],[1]]
print('#17')
print(np.dot(UUT17, y17))
print()
