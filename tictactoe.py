#Tic-Tac-Toe game. Author: Victor Manuel López Mayorga

from email.errors import FirstHeaderLineIsContinuationDefect
import math

from numpy import broadcast_arrays, full

def main():
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xx welcome to Tic-Tac-Toe xx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    board_size=int(input("digite the board size: "))
    grip=create_grid(board_size)
    count = 0
    player = "x"
    while prove_of_winner_diagonal(grip,board_size,player) and prove_of_winner_file(grip, board_size,player) and prove_of_winner_row(grip,board_size,player) and count<(board_size*board_size):
        if player == "x":
            player = "o"
        else :
            player = "x"
        choice=int(input(f"{player}'s turn to choose a square: "))
        play(player,choice, board_size,grip)
        count += 1
    if count == (board_size*board_size):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x game over, there is no winner x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    else :
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(f"x game over, player '{player}' is the winner x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    
def create_grid(board_size):
    count=0
    grip_list=[]
    file=[]
    for _ in range(board_size):
        for _ in range(board_size):
            count+=1
            file.append(count)
            if count < 10 :
                print(f" {count}|", end =" ")
            else :
                print(f"{count}|", end =" ")
        grip_list.append(file)
        file=[]
        print(end ="\n")
        for _ in range(board_size):
            print("_  ", end =" ")
        print(end ="\n")
    return grip_list

def play(player, choice, board_size, preview_list):
    x = math.ceil(choice/board_size) - 1
    if choice%board_size == 0 :
        y = board_size-1
    else :
        y = (choice%board_size) - 1
    preview_list[x][y] = player
    count = 0
    for i in range(board_size):
        for j in range(board_size):
            count+=1
            if count < 10 :
                print(f" {preview_list[i][j]}|", end =" ")
            else :
                print(f"{preview_list[i][j]}|", end =" ")
        print(end ="\n")
        for _ in range(board_size):
            print("_  ", end =" ")
        print(end ="\n")
    
def prove_of_winner_file(preview_list,board_size,player):
    for i in range(board_size) :
        count = 0
        for j in range(board_size) :
            if preview_list[i][j] == player :
                count += 1
        if count == board_size:
            return False
    return True

def prove_of_winner_row(preview_list,board_size, player):
    for i in range(board_size) :
        count = 0
        for j in range(board_size) :
            if preview_list[j][i] == player :
                count += 1
        if count == board_size:
            return False
    return True

def prove_of_winner_diagonal(preview_list,board_size, player):
    count = 0
    for i in range(board_size) :
        if preview_list[i][i] == player :
            count += 1
    if count == board_size:
        return False
    count = 0
    for i in range(board_size) :
        if preview_list[i][(board_size-1)-i] == player :
            count += 1
    if count == board_size:
        return False
    return True

if __name__ == "__main__":
    main()
