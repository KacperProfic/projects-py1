import random

def pickWord():
    with open('SOWPODS dic.txt', 'r') as f:
        words = f.readlines()
    return random.choice(words).strip()


def Hangman():
    word = pickWord()
    result = ['_'] * len(word)
    guessed_letters = set()
    tries_left = 6
    while tries_left != 0:
        
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

            if user_input not in word:
                tries_left -= 1
                print(f"Zostało Ci {tries_left} prób.")
            
            
            for i, letter in enumerate(word):
                if letter == user_input:
                    result[i] = user_input
                    
            if '_' not in result:
                print("Gratulacje! Odgadles slowo", word)
                break
    if tries_left == 0:
        print(f"Przegrałes! Słowo to {word}")

def main():
   
    while True:
        Hangman()
        answer = input("Chcesz zagrac jeszcze raz? Wpisz 'tak' aby kontynuowac: ")
        if answer.lower() != 'tak':
            print("Dzieki za gre!")
            break

if __name__ == "__main__":
   main()

