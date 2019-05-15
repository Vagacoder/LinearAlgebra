# 6.1 Inner Product, Length, and Orthogonality
import numpy as np

u = [-1, 2]
v = [4, 6]
w = [3, -1, -5]
x = [6, -2, 3]

# 1. u.u, v.u and (v.u)/(u.u)
print('#1')
print(np.inner(u, u))
print(np.inner(v, u))

# 7. ||w||
print('#7')
print(np.linalg.norm(w)**2)

# 8. ||x||
print('#8')
print(np.linalg.norm(x))

# 11. 
print('#11')
u11 = [7/4, 1/2, 1]
print(np.linalg.norm(u11)**2*16)

# 14.
print('#14')
u14 = [0, -5, 2]
v14 = [-4, -1, 8]
for i in range(len(u14)):
    u14[i] -= v14[i]
    
print(u14)
print(np.linalg.norm(u14)**2)

# 32
print('#32')
u32 = [1, 5,-3, 8]
v32 = [-7, 28, 9, -6]
a32 = [[0.5, 0.5, 0.5, 0.5],[0.5, 0.5, -0.5, -0.5],[0.5, -0.5, 0.5, -0.5],[0.5, -0.5, -0.5, 0.5]]
a32_1 = [0.5, 0.5, 0.5, 0.5]
a32_2 = [0.5, 0.5, -0.5, -0.5]
a32_3 = [0.5, -0.5, 0.5, -0.5]
a32_4 = [0.5, -0.5, -0.5, 0.5]
print('a1.a2 = ')
print(np.inner(a32_1, a32_2))
#print('a1.a3 = ' + np.inner(a32_1, a32_3))
#print('a1.a4 = ' + np.inner(a32_1, a32_4))
print('length of u')
lengthOfU = np.linalg.norm(u32)
print(lengthOfU)
print('length of Au')
lengthOfAU = np.linalg.norm(np.dot(a32, u32))
print(lengthOfAU)
print('length of v')
lengthOfV = np.linalg.norm(v32)
print(lengthOfV)
print('length of Av')
lengthOfAV = np.linalg.norm(np.dot(a32, v32))
print(lengthOfAV)
print('cosin of angle between u and v')
print(np.dot(u32, v32)/(lengthOfU * lengthOfV))
print('cosin of angle between Au and Av')
print(np.dot(np.dot(a32, u32), np.dot(a32, v32))/(lengthOfAU * lengthOfAV))

# 33
x33 = [[1, 3, -5, 0],[3, -6, 8, -11],[17,2, 9, 21],[-4, 5, 8, 11]]
print('x33 is:')
print(x33)

y33 = [[6, -4, -7, 9],[-10, 5, 2, 8],[6, 22, 7, -5],[-19, -3, -11, 16]]
v33 = [[7, -2, -6, -18],[-26, -2, 6, 19],[6, 3, -9, 11],[27, 5, 4, -17]]

print('(x.v/v.v)*v')
print(np.dot((np.inner(x33, v33)/np.inner(v33, v33)), v33))