width = int(input("Podaj szerokosc planszy: "))
height = int(input("Podaj wysokosc planszy: "))

def draw_board(width, height):
    for i in range(height):
        print(" ---" * width)
        print("|   " * (width + 1))
    print(" ---" * width)
    
draw_board(width, height)

