import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_char = string.punctuation

password = []

user = int(input("Enter a password length you want to create: "))

if user <= 0:
    print("Podaj dodatnia wartość: ")
    user = int(input("Enter a password length you want to create: "))

password.append(random.choice(lowercase))
password.append(random.choice(uppercase))
password.append(random.choice(digits))
password.append(random.choice(special_char))

all_char = lowercase + uppercase + digits + special_char
for _ in range(user - 4):
    password.append(random.choice(all_char))

random.shuffle(password)

final_password = ''.join(password)

print(f"Generated password: {final_password}")