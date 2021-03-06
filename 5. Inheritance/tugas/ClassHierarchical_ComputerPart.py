# Eusebia Nawang Ari
# 5210411195

# Hierarchical Inheritance
def rupiah(uang):
    x = str(uang)
    if len(x) <= 3:
        return "Rp." + x
    else:
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b


class ComputerPart:
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga


class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {rupiah(self.harga)}")


class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"Harga : {rupiah(self.harga)}")


class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {rupiah(self.harga)}")


p = Processor('Intel', 'Core i5 7740X', 8000000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODIMM PC19200/2400 MHz', 475000, "16 GB")
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500 GB', 7200)

parts = [p, ram, hdd]
print("\n\t\t\tHIERARCHIAL COMPUTER PART")
print("=================================================================================")
for part in parts:
    part.Tampil()
    print("")
print("=================================================================================\n")
