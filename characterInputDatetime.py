import datetime


x = input("Podaj imie: ")
y = int(input("Podaj wiek: "))

now = datetime.datetime.now()

year = now.year - y

print(f"{x} will be 100 years old on {year}")