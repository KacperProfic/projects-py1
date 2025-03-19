
def Hangman():
    word = 'EVAPORATE'
    result = ['_'] * len(word)
    guessed_letters = set()

    while True:
        try:
            print("Witaj w grze Hangman!")
            print(" ".join(result))
            
            user_input = input("Podaj litere: ").upper()

            if len(user_input) != 1 or not user_input.isalpha():
                print("Podaj pojedynczą literę.")
                continue
            if user_input in guessed_letters:
                print("juz odgadles te litere")
                continue
            guessed_letters.add(user_input)

            for i, letter in enumerate(word):
                if letter == user_input:
                    result[i] = user_input
                    
            if '_' not in result:
                print("Gratulacje! Odgadles slowo", word)
                break
        except ValueError:
            print("error")

Hangman()