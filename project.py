import random


#Global Data
possible_numbers = [1,2,3,4,5,6,7,8,9]
game_board = [[1,2,3],[4,5,6],[7,8,9]]
rows = 3
columns = 3
turn_counter = 0
game_active = True

#Print board on the screen
def board():
    for x in range(rows):
        print('\n ---+---+---')
        print('|', end="")
        for y in range(columns):
            print("", game_board[x][y], end=" |")
    print('\n ---+---+---')

#Choose game mode
def mode(player):
    while True:
        plyr = input(f"Who's Player {player}? :::").strip()
        if plyr.isalnum() == False:
            print("Name must be made of alphanumeric characters")
            pass
        else:
            if plyr == '':
                plyr = f"Player {player}"
                return plyr
            else:
                return plyr
        
#Modify game board
def modify(num, turn):
    num -= 1
    if (num == 0):
        game_board[0][0] = turn
    elif (num == 1):
        game_board[0][1] = turn
    elif (num == 2):
        game_board[0][2] = turn
    elif (num == 3):
        game_board[1][0] = turn
    elif (num == 4):
        game_board[1][1] = turn
    elif (num == 5):
        game_board[1][2] = turn
    elif (num == 6):
        game_board[2][0] = turn
    elif (num == 7):
        game_board[2][1] = turn
    elif (num == 8):
        game_board[2][2] = turn

def check_win(symbol):
    #rows
    if game_board[0][0] == symbol and game_board[0][1] == symbol and game_board[0][2] == symbol:
        return True
    elif game_board[1][0] == symbol and game_board[1][1] == symbol and game_board[1][2] == symbol:
        return True
    elif game_board[2][0] == symbol and game_board[2][1] == symbol and game_board[2][2] == symbol:
        return True
    
    #columns
    if game_board[0][0] == symbol and game_board[1][0] == symbol and game_board[2][0] == symbol:
        return True
    elif game_board[0][1] == symbol and game_board[1][1] == symbol and game_board[2][1] == symbol:
        return True
    elif game_board[0][2] == symbol and game_board[1][2] == symbol and game_board[2][2] == symbol:
        return True
    
    
    #Diagonal
    if game_board[0][0] == symbol and game_board[1][1] == symbol and game_board[2][2] == symbol:
        return True
    elif game_board[0][2] == symbol and game_board[1][1] == symbol and game_board[2][0] == symbol:
        return True

#Check for ties
def go_again():
    while True:
        global possible_numbers
        global game_board
        answer = input("It's a tie, do you want to go again? yes|y or no|n\n:::").strip().lower()
        if answer in ['yes', 'y']:
            possible_numbers = [1,2,3,4,5,6,7,8,9]
            game_board = [[1,2,3],[4,5,6],[7,8,9]]
            return True
        elif answer in ['no', 'n']:
            print("Thank you for playing, bye!")
            return False
        else:
            print("Input a valid answer")
            pass

#Inputs the data to modify the game board
def turn(player, symbol):
        board()
        while True:
            try:
                num = (int(input(f"{player}'s turn\nChoose a number [1-9]:::")))
                if 1 <= num <= 9 and num in possible_numbers:
                    modify(num, symbol)
                    possible_numbers.remove(num)
                    break
                else:
                    print("Invalid number, try again...")
                    pass
            except ValueError:
                print("Invalid input")
                pass
        board()
        global turn_counter
        turn_counter += 1

def main():
    print("TIC-TAC-TOE\n===========\n")
    player_1 = mode(1)
    player_2 = mode(2)
    while game_active:
        try:
            if turn_counter % 2 == 0:
                if possible_numbers == []:
                    go = go_again()
                    if go == True:
                        pass
                    else:
                        break
                turn(player_1, 'X')
                if check_win('X') == True:
                    print(f"{player_1} wins!!!")
                    break
                pass
            elif turn_counter % 2 == 1:
                if possible_numbers == []:
                    go = go_again()
                    if go == True:
                        pass
                    else:
                        break
                turn(player_2, 'O')
                if check_win('O') == True:
                    print(f"{player_2} wins!!!")
                    break
                pass
        except ValueError:        
            print("Invalid input, try again...\n")
            pass
        except KeyboardInterrupt or EOFError:
            exit()

if __name__=="__main__":
    main()