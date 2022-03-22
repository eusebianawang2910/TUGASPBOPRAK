#Eusebia Nawang Ari
#5210411195

# Implementasi Overriding

class Mahasiswa:
    def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim
    
    def tampilMhs(self):
        print("Nama : ", self.nama, ", nim :", self.nim)

    # method overloading
    def hitungSks(self, jmlsks = None, sks = None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks + sks
            print("Total SKS = ", totalsks)
        else : 
            totalsks = jmlsks
            print("Total SKS = ", totalsks)

class Mahasiswa2(Mahasiswa):
    def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim
    
    def tampilMhs(self):
        print(f'''
                Detail Mahasiswa
                Nama : {self.nama},
                NIM  : {self.nim}
                ''')

# memanggil class
mhs1 = Mahasiswa("Eusebia Nawang Ari", 5210411195)
mhs2 = Mahasiswa2("Aspin William Roy", 5200411287)

mhs1.tampilMhs()
mhs2.tampilMhs()

