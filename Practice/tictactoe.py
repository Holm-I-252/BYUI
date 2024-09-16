collumn_row = [':)', '1', '2', '3']
row_1 = ['A', ' ', ' ', ' ']
row_2 = ['B', ' ', ' ', ' ']
row_3 = ['C', ' ', ' ', ' ']

print(f"{collumn_row}\n{row_1}\n{row_2}\n{row_3}")

turn = 0

while " " in row_1 or " " in row_2 or " " in row_3:
    if turn == 0:
        move = input("Player 1, enter your move: ")
        if move[0] == "A":
            row_1[int(move[1])] = "X"
        elif move[0] == "B":
            row_2[int(move[1])] = "X"
        elif move[0] == "C":
            row_3[int(move[1])] = "X"
        turn = 1
    else:
        move = input("Player 2, enter your move: ")
        if move[0] == "A":
            row_1[int(move[1])] = "O"
        elif move[0] == "B":
            row_2[int(move[1])] = "O"
        elif move[0] == "C":
            row_3[int(move[1])] = "O"
        turn = 0
    print(f"{collumn_row}\n{row_1}\n{row_2}\n{row_3}")
    if row_1[1] == row_1[2] == row_1[3] == "X" or row_2[1] == row_2[2] == row_2[3] == "X" or row_3[1] == row_3[2] == row_3[3] == "X" or row_1[1] == row_2[1] == row_3[1] == "X" or row_1[2] == row_2[2] == row_3[2] == "X" or row_1[3] == row_2[3] == row_3[3] == "X" or row_1[1] == row_2[2] == row_3[3] == "X" or row_1[3] == row_2[2] == row_3[1] == "X":
        print("Player 1 wins!")
        break
    elif row_1[1] == row_1[2] == row_1[3] == "O" or row_2[1] == row_2[2] == row_2[3] == "O" or row_3[1] == row_3[2] == row_3[3] == "O" or row_1[1] == row_2[1] == row_3[1] == "O" or row_1[2] == row_2[2] == row_3[2] == "O" or row_1[3] == row_2[3] == row_3[3] == "O" or row_1[1] == row_2[2] == row_3[3] == "O" or row_1[3] == row_2[2] == row_3[1] == "O":
        print("Player 2 wins!")
        break
else:
    print("Game Over")

