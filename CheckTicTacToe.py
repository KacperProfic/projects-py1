def whoWins(lista):
    
    #check rows
    for i in range(3):
        if lista[i][0] == lista[i][1] == lista[i][2] and lista[i][0] != 0:
            return f"Player {lista[i][0]} won"
    #check columns
    for i in range(3):
        if lista[0][i] == lista[1][i] == lista[2][i] and lista[0][i] != 0:
            return f"Player {lista[0][i]} won"
    #check diagonal
    if lista[0][0] == lista[1][1] == lista[2][2] and lista[0][0] != 0:
        return f"Player {lista[0][0]} won"
    if lista[0][2] == lista[1][1] == lista[2][0] and lista[0][2] != 0:
        return f"Player {lista[0][2]} won"
    
    return "No winner"
print(whoWins([[2, 2, 0], [2, 1, 0], [2, 1, 1]]))
print(whoWins([[1, 2, 0], [2, 1, 0], [2, 1, 1]]))
print(whoWins([[0, 1, 0], [2, 1, 0], [2, 1, 1]]))
print(whoWins([[1, 2, 0], [2, 1, 0], [2, 1, 2]]))
print(whoWins([[1, 2, 0], [2, 1, 0], [2, 1, 0]]))