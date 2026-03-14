watt = int(input("Masukan penggunaan listrik (watt): "))
hour = int(input("Berapa jam sehari: "))
kwh = (watt * hour) / 1000
if (kwh < 100):
    print(kwh, "kwh")
    print("Total biaya",kwh * 0.10,"Dollar")
elif (kwh < 300):
    print(kwh, "kwh")
    print("Total biaya",kwh * 0.15,"Dollar")
elif (kwh >= 300):
    print(kwh, "kwh")
    print("Total biaya",kwh * 0.20,"Dollar")