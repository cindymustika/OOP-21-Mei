class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.krs = None

    def isi_krs(self, krs):
        self.krs = krs
        print(f'{self.nama} telah mengisi KRS.')

    def unduh_krs(self):
        if self.krs:
            print(f'{self.nama} mengunduh KRS:')
            self.krs.tampilkan_krs()
        else:
            print(f'{self.nama} belum mengisi KRS.')

class KRS:
    def __init__(self, semester):
        self.semester = semester
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, kode_mk, nama_mk, sks):
        self.mata_kuliah.append({'kode_mk': kode_mk, 'nama_mk': nama_mk, 'sks': sks})
        print(f'Mata kuliah {nama_mk} telah ditambahkan ke KRS semester {self.semester}.')

    def tampilkan_krs(self):
        print(f'KRS Semester {self.semester}')
        for mk in self.mata_kuliah:
            print(f"- {mk['kode_mk']}: {mk['nama_mk']} ({mk['sks']} SKS)")

# Contoh penggunaan kelas-kelas di atas

# Membuat instance dari kelas Mahasiswa
mahasiswa1 = Mahasiswa('2023001', 'Fiska Viola Nadila')
mahasiswa2 = Mahasiswa('2023002', 'Yosi Arjunita Putri')
mahasiswa3 = Mahasiswa ('2023003', 'Cindy Mustika Weny')

# Membuat instance dari kelas KRS untuk semester
krs1 = KRS('Ganjil 2023/2024')
krs2 = KRS('Genap 2023/2024')
krs3 = KRS ('Ganjil 2023/2024')

# Menambahkan mata kuliah ke KRS
krs1.tambah_mata_kuliah('IF101', 'Pengantar Informatika', 3)
krs1.tambah_mata_kuliah('IF102', 'Struktur Data', 4)
krs2.tambah_mata_kuliah('IF103', 'Basis Data', 3)
krs2.tambah_mata_kuliah('IF104', 'Algoritma dan Pemrograman', 4)
krs3.tambah_mata_kuliah('IF105', 'Embedded System', 3)
krs3.tambah_mata_kuliah('IF106', 'Object Oriented Programming', 4)

# Mahasiswa mengisi KRS
mahasiswa1.isi_krs(krs1)
mahasiswa2.isi_krs(krs2)
mahasiswa3.isi_krs(krs3)

# Mahasiswa mengunduh KRS
mahasiswa1.unduh_krs()
print()
mahasiswa2.unduh_krs()
mahasiswa3.unduh_krs()
