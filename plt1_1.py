import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


#zad 1 + 2

# x = np.arange(1, 21)
# y = 1/x
# plt.plot(x, y, 'g>', label='f(x)=1/x', linestyle=':')
# plt.axis(([0,20,0,1]))
# plt.ylabel("f(x)")
# plt.xlabel("x")
# plt.legend()
# plt.show()

#zad  3

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, label='sin(x)')
# plt.plot(x, z, label='cos(x)')
#
# plt.xlabel("x")
# plt.ylabel("funkcje trygonomteryczne")
#
# plt.legend()
# plt.show()

#zad 4

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.sin(x)
# plt.plot(x, y+1, label='sin(x)')
# plt.plot(x, (z+1)*-1, label='sin(x)')
#
# plt.xlabel("x")
# plt.ylabel("funkcje trygonomteryczne")
# plt.title('wykres sin(x), sin(x)')
#
# plt.legend()
# plt.show()

#zad 5

# df = pd.read_csv('iris.data', header=None)
# print(df.head())
#
# plt.scatter(x=df[0], y=df[1], s=abs(df[0]-df[1])*5, )
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()
