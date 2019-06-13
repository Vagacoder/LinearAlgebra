# 6.6 Application of Linear Model
import numpy as numpy
import sympy as sp


# 3
print('#3')
a3 = [[4, 2, 7],[2, 6, 10]]
b3 = sp.Matrix(a3).rref()
print(b3)
print()

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