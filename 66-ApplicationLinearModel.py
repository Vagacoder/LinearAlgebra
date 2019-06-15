# 6.6 Application of Linear Model
import numpy as np
import sympy as sp
import math


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
leastSol7 = np.concatenate((X7TX7, X7Ty7), axis=1)
print(leastSol7)
print(sp.Matrix(leastSol7).rref())
print()

#8
print('#8')
x8 = [[4, 4**2, 4**3],[6, 6**2, 6**3],[8, 8**2, 8**3],[10, 10**2, 10**3],
[12, 12**2, 12**3],[14, 14**2, 14**3],[16, 16**2, 16**3],[18, 18**2, 18**3]]
y8 = [[1.58],[2.08],[2.5],[2.8],[3.1],[3.4],[3.8],[4.32]]
x8T = np.transpose(x8)
x8Tx8 = np.dot(x8T, x8)
x8Ty8 = np.dot(x8T, y8)
leastSol8 = np.concatenate((x8Tx8, x8Ty8), axis=1)
print(leastSol8)
print(sp.Matrix(leastSol8).rref())
print()

# 11
print('#11')
x11 = [[1, 3*math.cos(0.88)],[1, 2.3*math.cos(1.1)],[1, 1.65*math.cos(1.42)],
[1, 1.25*math.cos(1.77)],[1, 1.01*math.cos(2.14)]]
y11 = [[3],[2.3],[1.65],[1.25],[1.01]]
x11T = np.transpose(x11)
x11Tx11 = np.dot(x11T, x11)
x11Ty11 = np.dot(x11T, y11)
leastSol11 = np.concatenate((x11Tx11, x11Ty11),axis=1)
print(leastSol11)
print(sp.Matrix(leastSol11).rref())
print()
