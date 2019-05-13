# 5.8 exercises
#7
import numpy as np

a = np.matrix('1 2; 3 4')
print(np.linalg.det(a))

b = [[1, 2],[3, 4]]
print(np.linalg.det(b))

c = [3, -1, 5]
print(np.linalg.norm(c)**2)