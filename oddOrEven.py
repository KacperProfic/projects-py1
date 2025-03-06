number = int(input("podaj liczbe: "))

if(number % 4 == 0 and number % 2 == 0):
    print("Wielokrotność 4 i liczba parzysta")
elif(number % 2 == 0):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")