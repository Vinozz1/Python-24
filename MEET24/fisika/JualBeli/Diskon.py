def hitung_diskon(diskon):
    def kurangi_diskon(harga):
        return harga - (harga * diskon / 100)
    return kurangi_diskon