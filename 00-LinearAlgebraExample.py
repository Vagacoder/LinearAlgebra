# 5.8 exercises
#7
import numpy as np
import sympy as sp

a = np.matrix('1 2; 3 4')
print('Ex.1 Construct matrix using "np.matrix()"')
print('and calculate determination:')
print(np.linalg.det(a))

b = [[1, 2],[3, 4]]
print('Ex.2 Construct matrix using 2D list')
print('and calculate determination:')
print(np.linalg.det(b))

c = [3, -1, 5]
print('Ex.3 Calculate norm / length of vector:')
print(np.linalg.norm(c)**2)

d = [[3, 5],[2, 9]]
print('Ex.4 Regular multiplication / dot:')
print(np.dot(b, d))

e = [-4, 1, -3, 8]
f = [3, 3, 5, -1]
print('Ex.5 inner product')
print(np.inner(e, f))

g = [[3, -2], [1, 6]]
h = [[-6], [3]]
print('Ex.6 reduced echelom form')
print(sp.Matrix([[3, -2, -6],[1, 6, 3]]).rref())

print('Ex.7 matrix transpose')
print(g)
print(np.transpose(g))