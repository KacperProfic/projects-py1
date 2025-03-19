
##########Program do gry w kółko i krzyżyk############

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
                        return"This field is already taken"
                else: 
                    return"Invalid input. Enter numbers between 1 and 3"
            except ValueError:
                return"Invalid input. Enter two numbers separated by a comma"
        game[row][col] = player
        player = 3 - player
        displayBoard(game)
    
        for i in range(3):
            if game[i][0] == game[i][1] == game[i][2] and game[i][0] != 0:
                return f"Player {game[i][0]} won"
            #check columns
        for i in range(3):
            if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0:
                return f"Player {game[0][i]} won"
            #check diagonal
        if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
            return f"Player {game[0][0]} won"
        if game[0][2] == game[1][1] == game[2][0] and game[0][2] != 0:
            return f"Player {game[0][2]} won"
        
    
    return "No winner"

def main():
    game_counter = 0
    player1_wins = 0
    player2_wins = 0
    while True:
        game_counter += 1
        print(f"Game {game_counter}")
        result = ticTacToeDraw()
        if result == 1:
            player1_wins += 1
            print("Player 1 won")
        elif result == 2:
            player2_wins += 1
            print("Player 2 won")
        else:
            print("No winner")
        
        print(f"Player 1 wins: {player1_wins}")
        print(f"Player 2 wins: {player2_wins}")
        
        answer = input("Do you want to play again? Enter 'yes' to continue: ")
        if answer.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
