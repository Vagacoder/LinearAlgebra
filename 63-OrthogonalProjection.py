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

# 25
u25 = [[-6, -3, 6, 1],[-1, 2, 1, -6],[3, 6, 3, -2],[6, -3, 6, -1],
[2, -1, 2, 3],[-3, 6, 3, 2],[-2, -1, 2, -3],[1, 2, 1, 6]]
y25 = [[1], [1], [1], [1], [1], [1], [1], [1]]
u25t = np.transpose(u25)
print('#25')
print(np.dot(np.dot(u25,u25t), y25))
print()

# 26
y26 = [[1], [1], [1], [1], [-1], [-1], [-1], [-1]]
print('#26')
print(np.dot(np.dot(u25,u25t), y26))
print()
