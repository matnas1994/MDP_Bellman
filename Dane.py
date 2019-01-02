class Dane:

    def __init__(self, sciezkaMapa):
        self.mapa = []
        with open(sciezkaMapa) as plik:
            for linia in plik:
                self.mapa.append(linia.strip().split())

    def okreslenie_typu_kazdego_z_pol(self):
        typ_kazdego_z_pol = []
        for i in range(1, int(self.mapa[0][1]) + 1):
            typ_kazdego_z_pol.append(self.mapa[i])
        return typ_kazdego_z_pol

    def okreslenie_R_kazdego_z_pola(self):
        wartosc_R_kazdego_z_pol = []
        wysokosc_mapy = int(self.mapa[0][1])
        for i in range(wysokosc_mapy + 2, wysokosc_mapy * 2 + 2):
            wartosc_R_kazdego_z_pol.append(self.mapa[i])
        return wartosc_R_kazdego_z_pol