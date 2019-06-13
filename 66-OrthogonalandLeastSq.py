# 6.6 Orthogonal and Least Squares
import numpy as np
import sympy as sp
import linearAlgebra as la 

# 7
print('#7')
X7 = [[1, 1],[2, 4],[3, 9],[4, 16],[5, 25]]
y7 = [[1.8],[2.7],[3.4],[3.8],[3.9]]
X7T = np.transpose(X7)
X7TX7 = np.dot(X7T, X7)
X7Ty7 = np.dot(X7T, y7)
leastSol = np.concatenate((X7TX7, X7Ty7), axis=1)
print(leastSol)
print(sp.Matrix(leastSol).rref())
print()
