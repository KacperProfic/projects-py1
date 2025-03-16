import random 

random4 = str(random.randint(1000, 9999))


print("witaj w grze!")

attempts = 0

while True:

    inp = input("podaj liczbe 4 cyfrowa: ")

    if not inp.isdigit() or len(inp) != 4:
        print("invalid input")
        continue
    attempts += 1

    cows = sum(1 for i in range(4) if inp[i] == random4[i])
    bulls = sum(1 for digit in inp if digit in random4) - cows

    print(f"{cows} cow(s), {bulls} bull(s)")

    if cows == 4:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

