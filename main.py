#Choice of x and o
choice = False
player1 = ''
player2 = ''
def game_choice():
    while choice == False:
        gamechoice = ['X', 'O']
        global player1
        player1 = input('Player1 choose x or o: ').upper()

        if player1 not in gamechoice:
            print('Please choose a either x or o: ')

        else:
            gamechoice.remove(player1)
            global player2
            player2 = gamechoice[0]

            return print(
                f'Player 1 chooses- {player1} and Player 2 chooses- {player2} and Firstly player 1 will choose followed by player 2')
                       #You could use a randint function to choose which player go first

# Board-
list1 = [['  |', '  |', ' '],
         ['  |', '  |', ' '],
         ['  |', '  |', ' ']]
def display_board():
    for i in range(0, 3):
        if i == 2:
            print(' '.join(list1[i]))  # New method to remove '' from a print statement

        else:
            print(' '.join(list1[i]))
            print('---------')


list3 = [['1  |', '2  |', '3 '],
         ['4  |', '5  |', '6 '],
         ['7  |', '8  |', '9 ']]
def display_positions():
    for i in range(0, 3):
        if i == 2:
            print(' '.join(list3[i]))  # New method to remove '' from a print statement

        else:
            print(' '.join(list3[i]))
            print('---------')


# Taking input
tic_tac_game=False
input1 = ''
choice_game = False
board_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_place_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
def take_input():
    while choice_game == False:
        global input1
        input1 = int(input('Please choose your marker place from 1-9 as shown below: '))
        if input1 in board_place:

            board_place.remove(input1)
            return
        else:
            print('Please choose the index from 1-9')


# checking win
def check_win():
    global tic_tac_game
    if list1[0][0] == list1[0][1] == list1[0][2] +' |' and list1[0][0]not in ['  |',' ']:
        if list1[0][0] == player1:
            tic_tac_game = True
            return print('Player1 won game ')
        else:
            tic_tac_game = True
            return print('Player 2 won game')
    elif list1[1][0] == list1[1][1] == list1[1][2]+' |' and list1[1][0]not in ['  |',' ']:
        if list1[1][0] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[2][0] == list1[2][1] == list1[2][2]+' |' and list1[2][0]not in ['  |',' ']:
        if list1[2][0] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[0][0] == list1[1][0] == list1[2][0] and list1[0][0]not in ['  |',' ']:
        if list1[0][0] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[0][1] == list1[1][1] == list1[2][1] and list1[0][1]not in ['  |',' ']:
        if list1[0][1] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[0][2] == list1[1][2] == list1[2][2] and list1[0][2] not in ['  |',' ']:
        if list1[0][2] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[0][0] == list1[1][1] == list1[2][2]+' |' and list1[0][0]not in ['  |',' ']:
        if list1[0][0] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    elif list1[0][2]+' |' == list1[1][1] == list1[2][0] and list1[0][2]not in ['  |',' ']:
        if list1[0][2] == player1+' |':
            tic_tac_game = True
            return print('Player1 won game')
        else:
            tic_tac_game = True
            return print('Player 2 won game')

    else:
        return print('No winer yet ')


# placement of choice in index
i=0
def tictactoe():
    game_choice()
    xando = [player1, player2, player1, player2, player1, player2, player1, player2, player1]
    i=0
    while tic_tac_game==False:

        display_board()
        print('')
        display_positions()
        take_input()
        input2 = board_place_dict[input1]
        if input2[1]==2:
            list1[input2[0]][input2[1]] = xando[i]
        else:
            list1[input2[0]][input2[1]] = xando[i]+' |'
        i+=1
        if i==9:
            print('')
            return print('The game is finished and no one won, try again😛: ')
        print('')
        check_win()
    else:
        return

tictactoe()
