import pandas as pd
import matplotlib.pyplot as plt

# zad 1

# data = pd.read_excel("./datasets/imiona.xlsx")
# wynik = data.groupby("Rok")["Liczba"].sum() / 1000
# print(wynik)
# wynik.plot(figsize=(6, 6), ylabel="liczba narodzin [tys.]", xticks=wynik.index, rot=45, grid=True, title="Tytuł")
# plt.show()

# zad 2

# data = pd.read_excel("./datasets/imiona.xlsx")
# wynik = data.groupby("Plec")["Liczba"].sum()
# print(wynik)
# wynik.plot(kind="bar", rot=0,title="całkowita liczba urodzin", ylabel="liczba urodzin")
# plt.show()

# zad 3

# data = pd.read_excel("./datasets/imiona.xlsx")
# wynik = data.groupby(["Rok","Plec"])["Liczba"].sum().sort_index(ascending=False).head(10).groupby("Plec").sum()
# wynik2= data[data["Rok"]>2012].groupby("Plec")["Liczba"]
# print(wynik2)
# wynik.plot(kind="pie",autopct="%.2f %%", ylabel="liczba urodzeń",title="całkowita liczb urodzeń w latach 2013-2017")
# plt.show()

# zad 4

# data=pd.read_csv("./datasets/zamowienia.csv", sep=";")
# wynik = data.groupby("Sprzedawca")["idZamowienia"].count()
# wynik.plot.barh(title="Liczba zamowień dla poszczególnych sprzedawców")
# print(wynik)
# plt.show()
