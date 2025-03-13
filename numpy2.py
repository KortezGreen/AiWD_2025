import numpy as np

# zad 1

# a = np.arange(3)
# b = np.arange(3)
# print(a * b)

# zad 2

# a = np.ndarray((3, 3))
# b = np.ndarray((4, 4))
# for i in range(3):
#     for j in range(3):
#         a[i][j] = np.random.randint(10, 51)
# for i in range(4):
#     for j in range(4):
#         b[i][j] = np.random.randint(10, 50)
# print('Macierz a: \n',a)
# print('Macierz b: \n',b)
# print(f"min(x) 3x3: {a.min(axis=1)} \nmin(x) 4x4: {b.min(axis=1)}")
# print(f"min(y) 3x3: {a.min(axis=0)} \nmin(y) 4x4: {b.min(axis=0)}")

# zad 3

# a = np.arange(3)
# b = np.arange(3)
# print(a.dot(b))

# zad 4

# a = np.array([1, 2, 3])
# b = np.array([1., 2., 3.])
# print(a * b)

# zad 5

# arr = np.arange(6).reshape((2, 3))
# a = np.sin(arr)
# print(a)

# zad 6

# arr = np.arange(6, 12).reshape((2, 3))
# b = np.cos(arr)
# print(b)

# zad 7

# arr = np.arange(6).reshape((2, 3))
# a = np.sin(arr)
# arr = np.arange(6, 12).reshape((2, 3))
# b = np.cos(arr)
# c = a + b
# print(c)

# zad 8

# a = np.arange(9).reshape((3, 3))
# for i in a:
#     print(i)

# zad 9

# a = np.arange(9).reshape((3, 3))
# for i in a.flat:
#     print(i)

# zad 10

# a = np.arange(81).reshape((9, 9))
# b = a.reshape((27, 3))
# c = a.reshape((3, 27))
# d = a.reshape((1, 81))
# e = a.reshape((81, 1))
# print(a, b, c, d, e, sep="\n")

# zad 11

# a = np.arange(12)
# b = a.reshape((3, 4))
# c = a.reshape((4, 3))
# d = a.reshape((2, 6))
# print('Przed spłaszczeniem: ', a, b, c, d, sep="\n")
# b = b.flatten()
# c = c.flatten()
# d = d.flatten()
# print('Po spłaszczeniu: ', a, b, c, d, sep="\n")
