gaji = int(input("Masukan gaji karyawan: "))
tahun = int(input("Masukan berapa tahun kerja: "))
if (tahun >= 10 ):
    print("Bonus: ", gaji * 0.25)
    print("Gaji plus bonus: ",(gaji * 0.25) + gaji)
elif (tahun >= 5 <= 9 ):
    print("Bonus: ", gaji * 0.15)
    print("Gaji plus bonus: ",(gaji * 0.15) + gaji)
elif (tahun >= 1 <= 4 ):
    print("Bonus: ", gaji * 0.05)
    print("Gaji plus bonus: ",(gaji * 0.05) + gaji)
elif (tahun < 1 ):
    print("No nonus")
    print("Gaji : ",gaji )