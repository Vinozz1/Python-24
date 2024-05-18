class EnergiPotensial:
    def __init__(self, massa, gravitasi, ketinggian):
        self.massa = massa
        self.gravitasi = gravitasi
        self.ketinggian = ketinggian

    def hitung(self):
        return self.massa * self.gravitasi * self.ketinggian
