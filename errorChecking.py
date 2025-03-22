import random

a = random.randint(1, 9)
uans = 0


while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 9: "))
            if guess >= 1 and guess <= 9:
                break
            else:
                print("Your input must be a number between 1 and 9 inlcusive")
        except ValueError:
            print("you must enter a number")
    uans += 1
    if guess == a:
        break
print(f"You needed {uans} guesses to guess the number {a}")


