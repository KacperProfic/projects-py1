import random

a = random.randint(1, 9)
uans = 0


while(uans != "exit" and uans != a):

    uans = input("Podaj cyfrę od 1-9(lub jesli chcesz wyjsc wpisz 'exit'): ")

    if uans == "exit":
        break

    uans = int(uans)


    if(uans < a):
        print("Podałes za mała cyfre")
    elif(uans > a):
        print("podałes za duza cyfre")
    else:
        print("Podałes poprawna cyfre")
        
input()
