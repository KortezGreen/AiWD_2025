import pandas as pd
import numpy as np

# 1
df = pd.read_excel('datasets/imiona.xlsx')
# print(df)

# 2a

# a=df['Liczba']
# print(df[a>1000])

# 2b

# b = df[df["Imie"] == "KACPER"]
# print(b)

# 2c

# c = df.agg({'Liczba': ['sum']})
# print(c)

# 2d

# d = df.groupby("Rok").agg({'Liczba': ['sum']})
# print(d)

# 2e

# e = df.groupby("Rok")["Liczba"].head(6).sum()
# print(e)

# 2f

# f = df.groupby("Plec")["Liczba"].sum()
# print(f)

# 2g

# g1= df[df["Plec"]=="K"].groupby("Imie")["Liczba"].sum().sort_values(ascending=False).head(1)
# g2= df[df["Plec"]=="M"].groupby("Imie")["Liczba"].sum().sort_values(ascending=False).head(1)
# print(g2, g1)

# 2h

g1 = df[df["Plec"]=="K"].groupby("Imie")["Liczba"].sum().sort_values(ascending=False).head(1)
g2 = df[df["Plec"]=="M"].groupby("Imie")["Liczba"].sum().sort_values(ascending=False).head(1)
g4 = df.groupby(["Rok"])[df["Plec"]=="M"].groupby("Imie")["Liczba"].sum().sort_values(ascending=False).head(1)
print(g4)

# 3

# df = pd.read_csv("./datasets/zamowienia.csv", sep=";")
# print(df)

# 3a

# a=df["Sprzedawca"].unique()
# print(a)

# 3b

# b = df["Utarg"].sort_values(ascending=False).head(5)
# print(b)

# 3c

# c = df.groupby("Sprzedawca")["idZamowienia"].count()
# print(c)

# 3d

# d = df.groupby("Kraj")["idZamowienia"].count()
# print(d)

# 3e

# e = df[(df.Kraj == "Polska") & (df['Data zamowienia'] > "2005")]["idZamowienia"].count()
# print(e)

# 3f

# f1 = df[(df['Data zamowienia'] < "2005") & (df['Data zamowienia'] > "2004")]["Utarg"].sum()
# f2 = df[(df['Data zamowienia'] < "2005") & (df['Data zamowienia'] > "2004")]["Utarg"].count()
# f3 = f1 / f2
# print(f3)

# 3g

# g2004 = df[(df['Data zamowienia'] < "2005") & (df['Data zamowienia'] > "2004")]
# g2005 = df[(df['Data zamowienia'] > "2005")]
# g2004.to_csv("./datasets/zamowienia_2004.csv")
# g2005.to_csv("./datasets/zamowienia_2005.csv")

