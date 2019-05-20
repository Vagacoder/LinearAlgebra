# 6.2 Orthogonal Sets
import numpy as np
import sympy as sp

# 6
u62 = [-4, 1, -3, 8]
u63 = [3, 3, 5, -1]
print('#6')
print(np.inner(u62, u63))

# 8
u81 = [3, 1]
u82 = [-2,6]
x8 = [-6, 3]
print('#8')
print(sp.Matrix([[3, -2, -6],[1, 6, 3]]).rref())

# 9
print('#9')
print(sp.Matrix([[1, -1, 2, 8],[0, 4, 1, -4],[1, 1, -2, -3]]).rref())

# 10
print('#10')
print(sp.Matrix([[3, 2, 1, 5],[-3, 2, 1, -3],[0, -1, 4, 1]]).rref())

# 35
print('#35')
u351 = [-6, -1, 3, 6, 2, -3, -2, 1]
u352 = [-3, 2, 6, -3, -1, 6, -1, 2]
u353 = [6, 1, 3, 6, 2, 3, 2, 1]
u354 = [1, -6, -2, -1, 3, 2, -3, 6]
print(np.inner(u351, u352))
print(np.inner(u351, u353))
print(np.inner(u351, u354))
print(np.inner(u352, u353))
print(np.inner(u352, u354))
print(np.inner(u353, u354))

# 36
print('#36')
u36 = [[-6, -3, 6, 1],[-1, 2, 1, -6],[3, 6, 3, -2],[6, -3, 6, -1],
[2, -1, 2, 3],[-3, 6, 3, 2],[-2, -1, 2, -3],[1, 2, 1, 6]]
u36t = np.transpose(u36)
print(np.dot(u36, u36t))
print(np.dot(u36t, u36))



