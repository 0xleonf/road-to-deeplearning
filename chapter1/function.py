import numpy as np

# matrix operation using list (not work)
print("Python list operation")
a = [1, 2, 3]
b = [4, 5, 6]

print("a+b", a+b)

try:
    print(a*b)
except TypeError:
    print("a*b has no meaning in python list")

print()

# matrix operation using numpy
print("numpy array operations:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a+b:", a+b)
print("a*b:", a*b)
print()

# sum by axis
print("sum by axis")
c = np.array([[1, 2, 3], [4, 5, 6]])
print('a:')
print(c)
print('c.sum(axis=0):', c.sum(axis=0))
print('c.sum(axis=1):', c.sum(axis=1))
print()

# broadcasting
print("broadcasting")
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print("a+b:\n", a+b)
