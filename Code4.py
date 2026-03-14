gaji = int(input("Masukan gaji: "))
kredit = int(input("Masukan nilai kredit: "))
kerja = int(input("Masukan berapa tahun bekerja: "))
if (gaji >= 3000 and kredit >= 650 and kerja >= 2 ):
    print("Pinjaman disetujui")
elif (gaji >= 3000 and kredit >= 650 and kerja < 2 ):
    print("Pinjaman disetujui dengan syarat")
elif (gaji >= 3000 and kredit < 650 and kerja >= 2 ):
    print("Pinjaman disetujui dengan syarat")
elif (gaji < 3000 and kredit >= 650 and kerja >= 2 ):
    print("Pinjaman disetujui dengan syarat")
elif (gaji >= 3000 and kredit < 650 and kerja < 2 ):
    print("Pinjaman ditolak")
elif (gaji < 3000 and kredit < 650 and kerja >= 2 ):
    print("Pinjaman ditolak")
elif (gaji < 3000 and kredit >= 650 and kerja < 2 ):
    print("Pinjaman ditolak")
elif (gaji < 3000 and kredit < 650 and kerja < 2 ):
    print("Pinjaman ditolak")