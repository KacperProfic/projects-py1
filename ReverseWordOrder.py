
x = input("Wpisz zdanie ktore chcesz odwrocic: ")

def ReverseWordOrder(x):
    split = x.split()
    reversed_words = split[::-1]
    return " ".join(reversed_words)
print(ReverseWordOrder(x))
