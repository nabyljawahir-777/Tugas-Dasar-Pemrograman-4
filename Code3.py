number1 = int(input("masukan sisi 1: "))
number2 = int(input("masukan sisi 2: "))
number3 = int(input("masukan sisi 3: "))
if (number3 != number1 != number2):
    print("A scalene triangle")
elif (number3 == number1 != number2):
    print("An isosceles triangle")
elif (number3 == number2 != number1):
    print("An isosceles triangle")
elif (number1 == number2 != number3):
    print("An isosceles triangle")
elif (number1 == number2 == number3):
    print("An equilateral triangle")