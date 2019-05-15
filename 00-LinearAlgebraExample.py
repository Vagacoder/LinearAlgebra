# 5.8 exercises
#7
import numpy as np

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