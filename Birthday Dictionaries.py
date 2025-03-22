import json


def birthday():
    print('Welcome to the birthday dictionary. We know the birthdays of:')

    with open("info.json", "r") as f:
        info = json.load(f)

    for name in info:
        print(name)
    name = input("Kogo daty urodzin potrzebujesz? ")
    
    if name in info.keys():
        print(info[name])
    else:
        print("Nie ma takiej osoby!")

    print("Chcesz dodac nowa osobe? Napisz 'y' jesli tak")
    answer = input()

    if answer == 'y':
        nameAdd = input("Podaj imie i nazwisko osoby: ")
        dateAdd = input("Podaj date urodzenia osoby w formacie DD-MM-YYYY: ")
        info[nameAdd] = dateAdd

        with open("info.json", "w") as f:
            json.dump(info, f, indent=4)



birthday()