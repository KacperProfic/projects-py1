number = int(input("podaj liczbe: "))

x = list(range(1, number + 1))

y = []

for elem in x:
    if number % elem == 0:
        y.append(elem)
print(y)