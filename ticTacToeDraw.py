def displayBoard(game):
    for row in game:
        print(" | ".join(str(cell) if cell != 0 else " " for cell in row))
        print ("-" * 5)

def ticTacToeDraw():

    game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O")
    print("Player 1 starts")
    player = 1
    for i in range(9):
        while True:
            try:
                user_input = input("Enter row and column number separated by a coma(','), type 'exit' to leave: ")
                if user_input.lower() == 'exit':
                        print("Goodbye")
                        return
                row, col = map(int, user_input.split(","))
                col -= 1
                row -= 1
                if row in range(3) and col in range(3):
                    if game[row][col] == 0:
                        break
                    else:
                        print("This field is already taken")
                else: 
                    print("Invalid input. Enter numbers between 1 and 3")
            except ValueError:
                print("Invalid input. Enter two numbers separated by a comma")
        game[row][col] = player
        player = 3 - player
        displayBoard(game)
    
        if i == 8:
            print("It's a draw")
ticTacToeDraw()