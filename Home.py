import numpy as np
import copy
from Dane import *
from Ruch import *


def obliczanie_t():
    for wiersz in range(0, szerokosc):
        for kolumna in range(0, dlugosc):
            if typ_kazdego_z_pol[wiersz][kolumna] != "2" and typ_kazdego_z_pol[wiersz][kolumna] != "0":
                linia = dlugosc * wiersz
                p = [0] * 4
                ruch = Ruch(linia, wiersz, kolumna, typ_kazdego_z_pol, ilosc_pol, dlugosc, szerokosc)
                p[0] = ruch.obliczanie_prawdopodbienstwa_gora()
                p[1] = ruch.obliczanie_prawdopodbienstwa_prawo()
                p[2] = ruch.obliczanie_prawdopodbienstwa_dol()
                p[3] = ruch.obliczanie_prawdopodbienstwa_lewo()
                t.append(p)
            else:
                t.append([[0]*12] * 4)

def porownanie_kosztow(v,vStare):
    for i in range(0, szerokosc):
        for j in range(0, dlugosc):
            if abs(float(v[0][0]) - float(vStare[0][0])) < 0.0001:
                    return 1
    return 0



dane = Dane("MDP_mapa.txt")
typ_kazdego_z_pol = dane.okreslenie_typu_kazdego_z_pol()
r = dane.okreslenie_R_kazdego_z_pola()
szerokosc = int(dane.mapa[0][1])
dlugosc = int(dane.mapa[0][0])
ilosc_pol = szerokosc*dlugosc
t = []*ilosc_pol
polityka_ruchu = [[0 for col in range(4)] for row in range(3)]
v = copy.deepcopy(r)
obliczanie_t()

for licznik in range(0, 1000):
    vStare = copy.deepcopy(v)
    for wiersz in range(0, szerokosc):
        for kolumna in range(0, dlugosc):
            if typ_kazdego_z_pol[wiersz][kolumna] != "2" and typ_kazdego_z_pol[wiersz][kolumna] != "0":
                linia = dlugosc * wiersz
                suma = [0]*4
                for k in range(0, 4):
                    for l in range(0, 12):
                         w = int(l/dlugosc)
                         s = l % dlugosc
                         suma[k] = suma[k] + t[kolumna + linia][k][l] * float(v[w][s])
                pi = int(np.argmax(suma))
                gamma = 0.5
                v[wiersz][kolumna] = float(r[wiersz][kolumna]) + gamma * suma[pi]
                polityka_ruchu[wiersz][kolumna] = pi + 1
    if porownanie_kosztow(v,vStare) == 1:
        break



#wywietlanie
print(str(dlugosc)+" "+str(szerokosc))

for wiersz in range(0, szerokosc):
    napis = ""
    for kolumna in range(0, dlugosc):
        napis += " "+str(typ_kazdego_z_pol[wiersz][kolumna])
    print(napis)

print()

for wiersz in range(0, szerokosc):
    napis = ""
    for kolumna in range(0, dlugosc):
        napis += " "+str(r[wiersz][kolumna])
    print(napis)

print()

for wiersz in range(0, ilosc_pol):
    for kolumna in range(0, 4):
            napis = ""
            for k in  range(0, 12):
                napis += " {:.1f}".format(float (t[wiersz][kolumna][k]))
            print(napis)
    print()


print("Mapa Potecjałów:")
for wiersz in range(0, szerokosc):
    napis = ""
    for kolumna in range(0, dlugosc):
        napis += " {:.2f}".format(float(v[wiersz][kolumna]))
    print(napis)

print()

print("Polityka ruchu: (1, 2, 3, 4 to odpowiednio ruch do góry, w prawo, w dół, w lewo)")
for wiersz in range(0, szerokosc):
    napis = ""
    for kolumna in range(0, dlugosc):
        napis += " "+str(polityka_ruchu[wiersz][kolumna])
    print(napis)






