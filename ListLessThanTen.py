a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c =[]
for i in a:
    if i < 5:
        b.append(i)
print(b)

number = int(input("Podaj liczbe:"))

for i in a:
    if i < number:
        c.append(i)
print(c)

