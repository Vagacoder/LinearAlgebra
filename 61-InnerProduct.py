# 6.1 Inner Product, Length, and Orthogonality
import numpy as np

u = [-1, 2]
v = [4, 6]
w = [3, -1, -5]
x = [6, -2, 3]

# 1. u.u, v.u and (v.u)/(u.u)
print(np.inner(u, u))
print(np.inner(v, u))

# 7. ||w||
print(np.linalg.norm(w)**2)

# 8. ||x||
print(np.linalg.norm(x))

# 11. 
u11 = [7/4, 1/2, 1]
print(np.linalg.norm(u11)**2*16)

# 14.
u14 = [0, -5, 2]
v14 = [-4, -1, 8]
for i in range(len(u14)):
    u14[i] -= v14[i]
    
print(u14)
print(np.linalg.norm(u14)**2)