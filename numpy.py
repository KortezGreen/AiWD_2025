import numpy as np

# #z1
# a=np.arange(2,41,2)
# print(a)

# #z2
# a=[2.3,3.4,2.7]
# print(a)
# b=np.array(a,dtype='int64')
# print(b)

# #z3
# def zad3(n):
#     return np.arange(1,(n*n)+1)
# c=3
# print(zad3(c))

#zad 4
# def generuj(a,b):
#     return np.logspace(start=1,stop=b,num=b,base=a,dtype='int64')
# print(generuj(2,4))

#zad 5
def zad5(n):
    macierz = np.arange(n,0,-1)
    macierz = np.diag(macierz)
    return macierz
n=3
print(zad5(n))

#zad 5
