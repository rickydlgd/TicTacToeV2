import random
import time

menu_prompt = '\nTic-Tac-Toe? Y or N: '

the_board = {
    '7': ' ',
    '8': ' ',
    '9': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '1': ' ',
    '2': ' ',
    '3': ' ',
}

# computer_options = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
computer_options = []

computer_selection = []
player_selection = []


def player_1():
    player_options = ['7', '8', '9', '4', '5', '6', '1', '2', '3', 'help']
    player_prompt = "\nMake your move (type 'help' for the board visual): "
    player_choice = input(player_prompt)
    for choice in player_choice:
        if player_choice == 'help':
            while player_choice == 'help':
                player_help()
                player_choice = input(player_prompt)
        elif player_choice not in player_options:
            while player_choice not in player_options:
                print("\nTry again.")
                player_choice = input(player_prompt)
        elif player_choice in computer_selection:
            while player_choice in computer_selection:
                print("\nThat spot's taken.")
                player_choice = input(player_prompt)
    for choice_2 in player_choice:
        if player_choice in computer_options:
            computer_options.remove(player_choice)
        if player_choice not in player_selection:
            player_selection.append(player_choice)
            the_board[player_choice] = 'X'


def player_2():
    computer_choice = ''
    options_len = len(computer_options)
    if options_len > 0:
        computer_choice = random.choice(computer_options)
        computer_selection.append(computer_choice)
        the_board[computer_choice] = 'O'
        if computer_choice in computer_options:
            computer_options.remove(computer_choice)
    else:
        print("\nI'm out of options!")


def player_help():
    board_visual()


def board_visual():
    print("""\nBoard Visual:
    
         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3
    """)


def lets_play():
    player_1()
    print_board(the_board)
    print('')
    time.sleep(1)
    player_2()
    print_board(the_board)


def print_board(board):
    print(f"\n        {the_board['7']}" + ' | ' + f"{the_board['8']}" + ' | ' + f"{the_board['9']}")
    print("       -----------")
    print(f"        {the_board['4']}" + ' | ' + f"{the_board['5']}" + ' | ' + f"{the_board['6']}")
    print("       -----------")
    print(f"        {the_board['1']}" + ' | ' + f"{the_board['2']}" + ' | ' + f"{the_board['3']}")


def game_in_session():
    game_on = True
    while game_on:
        lets_play()
        if the_board['7'] == 'X' and the_board['8'] == 'X' and the_board['9'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['7'] == 'O' and the_board['8'] == 'O' and the_board['9'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['4'] == 'X' and the_board['5'] == 'X' and the_board['6'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['4'] == 'O' and the_board['5'] == 'O' and the_board['6'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['1'] == 'X' and the_board['2'] == 'X' and the_board['3'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['1'] == 'O' and the_board['2'] == 'O' and the_board['3'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['7'] == 'X' and the_board['4'] == 'X' and the_board['1'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['7'] == 'O' and the_board['4'] == 'O' and the_board['1'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['8'] == 'X' and the_board['5'] == 'X' and the_board['2'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['8'] == 'O' and the_board['5'] == 'O' and the_board['2'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['9'] == 'X' and the_board['6'] == 'X' and the_board['3'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['9'] == 'O' and the_board['6'] == 'O' and the_board['3'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['7'] == 'X' and the_board['5'] == 'X' and the_board['3'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['7'] == 'O' and the_board['5'] == 'O' and the_board['3'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif the_board['9'] == 'X' and the_board['5'] == 'X' and the_board['1'] == 'X':
            print('\nYou won!')
            game_on = False
            break
        elif the_board['9'] == 'O' and the_board['5'] == 'O' and the_board['1'] == 'O':
            print('\nYou lost!')
            game_on = False
            break
        elif len(computer_options) == 0:
            print("It's a tie!")
            game_on = False
            break


def menu():
    selection = input(menu_prompt)
    clear_board = the_board
    while selection != 'n':
        if selection == 'y':
            player_instructions = """\nPlace your move by typing one of the following: 
    7, 8, 9, 
    4, 5, 6, 
    1, 2, 3
    
    Here is a visual of the board with your options:

                 7 | 8 | 9
                -----------
                 4 | 5 | 6
                -----------
                 1 | 2 | 3"""
            print(player_instructions)
            computer_options.extend(['7', '8', '9', '4', '5', '6', '1', '2', '3'])
            game_in_session()
            for x in computer_options:
                computer_options.remove(x)
            clear_board.clear()
            clear_board['7'] = ' '
            clear_board['8'] = ' '
            clear_board['9'] = ' '
            clear_board['4'] = ' '
            clear_board['5'] = ' '
            clear_board['6'] = ' '
            clear_board['1'] = ' '
            clear_board['2'] = ' '
            clear_board['3'] = ' '
            player_selection.clear()
            computer_selection.clear()
        else:
            print("\nInvalid command.")
        selection = input(menu_prompt)
    print("\nSee you next time!")

menu()