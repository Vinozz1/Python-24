class EnergiKinetik:
    def __init__(self, massa, kecepatan):
        self.massa = massa
        self.kecepatan = kecepatan

    def hitung(self):
        return 0.5 * self.massa * (self.kecepatan ** 2)
