# ============================================================
#
# Student Name (as it appears on cuLearn): Salim Erradi
# Student ID (9 digits in angle brackets): <101071241>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

import pygame

'''
This function loads a returns a initialized board.

@params     None
@return     the board position list ( 2d array )

'''

def init_board():
    board = []
    board_position = []
    counter = 0

    #Makes two dimensional array
    for x in range(8):
        board = []
        for y in range(8):

            board.append(y)
            #Adding element
        board_position.append(board)

    return board_position

'''
This function prints out the menu system.

@params     board_position, list of positions on the board, check, check to see if the board has been entered
@return     returns choice of the user

'''

def menu_system(board_position,check):

    print ("- MENU SYSTEM -")
    print ("- PRESS 1 TO LOAD A BOARD -")
    print ("- PRESS 2 TO RECIEVE INSTRUCTIONS-")
    print ("- PRESS 3 TO MOVE PIECE -")
    print ("- PRESS 4 TO QUIT -")

    choice = input("Choice: ")

    return choice

'''
This function prints the board.

@params     board_position the list containing the position of the boards
@return     updated list of the board

'''

def print_board(board_position):
    print ("00000000000000000000000000000000")
    print()
    print ("       1 2 3 4 5 6 7 8")
    for row in range (len(board_position)):
        print()
        #print the letter position in that row so first row A second row B
        print (chr(65+row),"    ",end = " ")
        for column in range (len(board_position)):
            print (board_position[row][column],end = " ")
    print ()
    print ()
    print ("00000000000000000000000000000000")

    return board_position

'''
This function takes user's input of user making the board and prints out who is winning.

@params     board_position, the boards positions
@return     Updated list of the board position

'''

def user_input(board_position):


    white_pieces = ["-","k","q","p","r","b","n"]
    black_pieces = ["K","Q","P","R","B","N"]
    full_set = black_pieces + white_pieces
    counter = 1
    totalsum_w = 0
    totalsum_b = 0
    #Ask user to make board
    make_board = input("Make your board: \n")
    #While length of the board row is not 8 prompt the user again
    while len(make_board)!=8 or make_board[0] not in full_set or make_board[1] not in full_set or make_board[2] not in full_set or make_board[3] not in full_set or make_board[4] not in full_set or make_board[5] not in full_set or make_board[6] not in full_set or make_board[7] not in full_set:

        print("Length not 8 or Not Correct piece inputted")

        make_board = input()

    #Finds the sum of the white pieces and black pieces
    totalsum_w = white_piece_sum(make_board)
    totalsum_b = black_piece_sum(make_board)
    #Sets the board position to a value such as "-" or a "queen" or a "knight"
    for x in range (len(make_board)):
        board_position[counter-1][x] = make_board[x]
    #While counter is less than 8 it keeps asking the user to make rows for their board
    while counter < 8:
        make_board = input()

        while len(make_board)!=8 or make_board[0] not in full_set or make_board[1] not in full_set or make_board[2] not in full_set or make_board[3] not in full_set or make_board[4] not in full_set or make_board[5] not in full_set or make_board[6] not in full_set or make_board[7] not in full_set:

            print("Length not 8 OR Not correct piece inputted")

            make_board = input()

        totalsum_w += white_piece_sum(make_board)
        totalsum_b += black_piece_sum(make_board)
        counter+=1
        #Sets board value to that position
        for x in range (len(make_board)):
            board_position[counter-1][x] = make_board[x]

    print_board(board_position)

    print ("White Piece Sum: ", totalsum_w)
    print ("Black Piece Sum: " , totalsum_b)

    decide_winner(totalsum_b,totalsum_w)

    return board_position

'''
This function returns the White piece total.

@params     make_board, the board that the user is creating
@return     the sum of the all the white pieces

'''
def white_piece_sum(make_board):
    sum_for_w = 0
    #Used to add up numbers in order to get total sum of white pieces
    for i in range(len(make_board)):

        if make_board[i] == "k":
            sum_for_w += 0

        elif make_board[i] == "q":
            sum_for_w += 10

        elif make_board[i] =="r":
            sum_for_w += 5

        elif make_board[i] == "b":
            sum_for_w += 3

        elif make_board[i] == "p":
            sum_for_w += 1

        elif make_board[i] == "n":
            sum_for_w += 3.5

    return sum_for_w
'''
This function returns the total black piece sum

@params     make_board, the board that the user is creating
@return     black piece total
'''
def black_piece_sum(make_board):
    sum_for_b = 0
    #Used to add up total for black pieces

    for i in range(len(make_board)):
        if make_board[i] == "K":
            sum_for_b += 0

        elif make_board[i] == "Q":
            sum_for_b += 10

        elif make_board[i] =="R":
            sum_for_b += 5

        elif make_board[i] == "B":
            sum_for_b += 3

        elif make_board[i] == "P":
            sum_for_b += 1

        elif make_board[i] == "N":
            sum_for_b += 3.5


    return sum_for_b
'''
This function finds winner between black and white pieces.

@params    black_pieces, list that includes the characters in chess that are black , white_pieces, list that includes the characters in chess that are white
@return    None

'''
def decide_winner(black_pieces,white_pieces):
    if black_pieces > white_pieces:
        print("Black pieces are currently winning.")
    elif black_pieces < white_pieces:
        print("White pieces are currently winning")
    else:
        print("It is currently a tie.")
'''
This function moves a piece.

@params     board_position, the positions on the board
@return     board_position, the new updated list of positions

'''

def move_pieces(board_position):
    sum_for_b = 0
    sum_for_w = 0
    alpha = ["A","B","C","D","E","F","G","H"]
    print("Current board.")
    print_board(board_position)

    position = input("Which piece would you like to move? (Type coordinate) ")

    #Checks to see if postion is gsreater then two or less then two, if the correct input is in and if the board_position is not equal to nothing
    while len(position) != 2 or position[0] not in alpha or int(position[1]) > 8 or int(position[1]) < 1 or board_position[ord(position[0])-65][int(position[1])-1] == "-" :

        print("INVALID COORDINATES OR YOU HAVE PICKED A LOCATION WHERE IT IS BLANK")
        position = input("Which piece would you like to move?")

    holder = board_position[ord(position[0])-65][int(position[1])-1]
    #Takes the ord version the of position and substracts to get value Ex ord("A") - 1 gives 0 so row 0 so position[0] - 1 to get row and position[1] - 1 to get column in 2D array
    board_position[ord(position[0])-65][int(position[1])-1]= "-"

    newposition = input("What new location would you like to move that piece to?")
    while len(newposition) != 2 or newposition[0] not in alpha or int(newposition[1]) > 8 or int(newposition[1]) < 1 or board_position[ord(newposition[0])-65][int(newposition[1])-1] == "-":
        print("INVALID COORDINATES. HAVE TO PICK LOCATION WHERE THERE IS A PIECE")
        newposition = input("Which piece would you like to move?")

    board_position[ord(newposition[0])-65][int(newposition[1])-1] = holder

    for row in range(8):
        for column in range(8):
            if board_position[row][column] == "K":
                sum_for_b += 0

            elif board_position[row][column]== "Q":
                sum_for_b += 10

            elif board_position[row][column]=="R":
                sum_for_b += 5

            elif board_position[row][column] == "B":
                sum_for_b += 3

            elif board_position[row][column] == "P":
                sum_for_b += 1

            elif board_position[row][column]== "N":
                sum_for_b += 3.5

    for row in range(8):
        for column in range(8):
            if board_position[row][column] == "k":
                sum_for_w += 0

            elif board_position[row][column]== "q":
                sum_for_w += 10

            elif board_position[row][column]=="r":
                sum_for_w += 5

            elif board_position[row][column] == "b":
                sum_for_w += 3

            elif board_position[row][column] == "p":
                sum_for_w += 1

            elif board_position[row][column]== "n":
                sum_for_w += 3.5



    print ("New Board")
    print ("White Piece Sum: ", sum_for_w)
    print ("Black Piece Sum: " , sum_for_b)

    decide_winner(sum_for_b,sum_for_w)
    print_board(board_position)

    return board_position

'''

This function shows instructions to the user

@params     None
@return     None

'''
def instructions():
    print("You will be moduling a chess game in progress.")
    print("If you load board you will input an 8 by 8 board by hand by typing - for blank space and any k,q,r,b,n,p character as well.")
    print("Lowercase letters such as k (King),q (Queen),r (Rook),b (bishop),n (knight),p (pawn) represent white pieces. Black pieces are represented by uppercase letters of the characters mentioned before.")
    print("After you display board it will tell you both sides total point and who is currently winning.")
    print("User will also have the right to move piece if she/he wants to desingated area. By typing (Letter,Number)")
    print("Have fun!!!")
'''
This function is the main

@params     None
@return     None

'''

def main():

    check = False
    if check == False:
        board_position = []
    else:
        pass
    choice = menu_system(board_position,check)

    while choice != "4":

        if  choice == "1":
            check = True

            board_pos = init_board()
            user_board = user_input(board_pos)
            choice = menu_system(board_position,check)

        elif choice == "2":
            instructions()
            choice = menu_system(board_position,check)

        elif choice == "3":
            if check == True:
                move_pieces(user_board)
                choice = menu_system(board_position,check)

            else:
                print("You have to create board first.")
                choice = menu_system(board_position,check)


        else:
            print("Not a valid option.")
            choice = menu_system(board_position,check)

main()
