vehicle = input("Masukan jenis kendaraan (motor/car/bus): ")
hours = int(input("Masukan waktu (jam): "))
BiayaParkir = 1
TambahanBiaya = 0.5
if (hours <= 1 and vehicle == "motor"):
    print("Biaya parkir: ", BiayaParkir)
elif (hours > 1 and vehicle == "motor"):
    print("jam pertama: ", BiayaParkir)
    print("biaya per jam: ", TambahanBiaya)
    print("Biaya parkir 1 jam lebih: ",BiayaParkir + ((hours - 1) * TambahanBiaya))
elif (hours <= 1 and vehicle == "car"):
    print("Biaya parkir: ", BiayaParkir + 1)
elif (hours > 1 and vehicle == "car"):
    print("jam pertama: ", BiayaParkir + 1)
    print("biaya per jam: ", TambahanBiaya + 0.5)
    print("Biaya parkir 1 jam lebih: ",(BiayaParkir + 1) + ((hours - 1) * (TambahanBiaya + 0.5)))
elif (hours <= 1 and vehicle == "bus"):
    print("Biaya parkir: ", BiayaParkir + 1)
elif (hours > 1 and vehicle == "bus"):
    print("jam pertama: ", BiayaParkir + 2)
    print("biaya per jam: ", TambahanBiaya + 1.5)
    print("Biaya parkir 1 jam lebih: ",(BiayaParkir + 2) + ((hours - 1) * (TambahanBiaya + 1.5)))