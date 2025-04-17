import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


#zad 6

data = pd.read_excel("imiona.xlsx")
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

x1 = data['Plec']
y1 = data['Liczba']
c = ['pink', 'blue']

plt.bar(x1, y1, color=c)
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')
plt.show()


