class Mobil:
    warna = "belum"
    merek = "belum"
    kecepatan = 0
    spion = "belum"
    ban = "belum"
    ac = "belum"

    def cetak_pasti(fungsi):
        def pembungkus():
            print("pasang spion kuda")
            spion = "kuda"
            fungsi()
            print("pasang ban michelin")
            ban = "michelin"
        return pembungkus()
    
    @cetak_pasti
    def dicat():
        print("sedang dicat")

    def __init__(this, warna = "Merah", merek = "Audi", kecepatan = 160):
        this.warna = warna
        this.merek = merek
        this.kecepatan = kecepatan

    @staticmethod
    def lihat_variabel_bawaan():
        return ["warna", "merek", "kecepatan", "spion", "ban", "ac"]
    
    @classmethod
    def lihat_parameter_input(cls):
        return cls.warna
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def tambah_kecepatan(self):
        self.kecepatan += 50

    def nos(self):
        super().tambah_kecepatan()
        self.tambah_kecepatan()

mobil_1 = Mobil(kecepatan=170)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

print(Mobil.lihat_variabel_bawaan())

print(mobil_1.lihat_parameter_input())

print(Mobil.lihat_parameter_input())

print(mobil_1.tambah_kecepatan())

print(mobil_1.kecepatan)

f1 = MobilSport(merek="Ferrari", kecepatan=200)

print(f1.merek)
print(f1.kecepatan)

f1.tambah_kecepatan()

print(f1.kecepatan)

f1.nos()

print(f1.kecepatan)

"""
Output:
Merah
DicodingCar
160
"""