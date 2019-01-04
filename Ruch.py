class Ruch:

    def __init__(self, linia, wiersz, kolumna, typ_kazdego_z_pol, ilosc_pol,dlugosc, szerokosc):
        self.linia = linia
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.typ_kazdego_z_pol = typ_kazdego_z_pol
        self.ilosc_pol = ilosc_pol
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def obliczanie_prawdopodbienstwa_gora(self):
        g = [0] * self.ilosc_pol
        if self.wiersz == 0:
            g[self.kolumna + self.linia] += 0.8

        if self.kolumna == 0:
            g[self.kolumna + self.linia] += 0.1

        if self.kolumna + 1 != self.dlugosc:
            if self.typ_kazdego_z_pol[self.wiersz][self.kolumna + 1] == "0":
                g[self.kolumna + self.linia] += 0.1

            if self.typ_kazdego_z_pol[self.wiersz][self.kolumna - 1] == "0":
                g[self.kolumna + self.linia] += 0.1

            if self.typ_kazdego_z_pol[self.wiersz - 1][self.kolumna] == "0":
                g[self.kolumna + self.linia] += 0.8

            if (self.kolumna + self.linia + 1) % 4 != 0 and self.typ_kazdego_z_pol[self.wiersz][self.kolumna + 1] != "0":
                g[self.kolumna + 1 + self.linia] += 0.1

        if ((self.kolumna + self.linia) - 1) >= self.linia and self.typ_kazdego_z_pol[self.wiersz][self.kolumna - 1] != "0":
            g[self.kolumna + self.linia - 1] += 0.1

        if self.wiersz > 0 and self.typ_kazdego_z_pol[self.wiersz - 1][self.kolumna] != "0":
            g[self.kolumna + self.linia - self.dlugosc] += 0.8

        if ((self.kolumna + self.linia + 1) % self.dlugosc == 0):
            g[self.kolumna + self.linia] += 0.1

        return g


    def obliczanie_prawdopodbienstwa_prawo(self):
        p = [0] * self.ilosc_pol
        if ((self.kolumna + self.linia + 1) % self.dlugosc == 0) or self.typ_kazdego_z_pol[self.wiersz][self.kolumna + 1] == "0":
            p[self.kolumna + self.linia] += 0.8
        else:
            p[self.kolumna + self.linia + 1] += 0.8

        if self.wiersz == 0:
            p[self.kolumna + self.linia] += 0.1
        else:
            if self.typ_kazdego_z_pol[self.wiersz - 1][self.kolumna] != "0":
                p[self.kolumna + self.linia - self.dlugosc] += 0.1
            else:
                p[self.kolumna + self.linia] += p[self.kolumna + self.linia] + 0.1

        if self.wiersz + 1 < 3 and self.typ_kazdego_z_pol[self.wiersz + 1][self.kolumna] != "0":
            p[self.kolumna + self.linia + self.dlugosc] += 0.1

        if self.wiersz + 1 < 3 and self.typ_kazdego_z_pol[self.wiersz + 1][self.kolumna] == "0":
            p[self.kolumna + self.linia] += 0.1

        if self.wiersz == (self.szerokosc - 1):
            p[self.kolumna + self.linia] += 0.1

        return p


    def obliczanie_prawdopodbienstwa_dol(self):
        d = [0] * self.ilosc_pol
        if self.wiersz != (self.szerokosc - 1) and self.typ_kazdego_z_pol[self.wiersz + 1][self.kolumna] != "0":
            d[self.kolumna + self.linia + self.dlugosc] += 0.8
        else:
            d[self.kolumna + self.linia] += 0.8

        if (self.kolumna + self.linia) % self.dlugosc == 0:
            d[self.kolumna + self.linia] += 0.1
        else:
            if self.typ_kazdego_z_pol[self.wiersz][self.kolumna - 1] != "0":
                d[self.kolumna + self.linia - 1] += 0.1
            else:
                d[self.kolumna + self.linia] += 0.1

        if (self.kolumna + self.linia + 1) % self.dlugosc != 0 and self.typ_kazdego_z_pol[self.wiersz][self.kolumna + 1] != "0":
            d[self.kolumna + self.linia + 1] += 0.1
        else:
            d[self.kolumna + self.linia] += 0.1

        return d


    def obliczanie_prawdopodbienstwa_lewo(self):
        l = [0] * self.ilosc_pol
        if (self.kolumna == 0 or (self.kolumna + self.linia) % self.dlugosc == 0) or self.typ_kazdego_z_pol[self.wiersz][self.kolumna - 1] == "0":
            l[self.kolumna + self.linia] += 0.8
        else:
            l[self.kolumna + self.linia - 1] += 0.8

        if self.wiersz == 0:
            l[self.kolumna + self.linia] += 0.1
        else:
            if self.typ_kazdego_z_pol[self.wiersz - 1][self.kolumna] == "0":
                l[self.kolumna + self.linia] += 0.1
            else:
                l[self.kolumna + self.linia - self.dlugosc] += 0.1

        if self.wiersz == (self.szerokosc - 1):
            l[self.kolumna + self.linia] += 0.1
        else:
            if self.typ_kazdego_z_pol[self.wiersz + 1][self.kolumna] == "0":
                l[self.kolumna + self.linia] += 0.1
            else:
                l[self.kolumna + self.linia + self.dlugosc] += 0.1

        return l