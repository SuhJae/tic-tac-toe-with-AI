# Import the random module
import random

# Define variables
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = "X"
turn = 0

# Class for colors
class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    white = '\033[97m'
    reset = '\033[0m'

# Class for background colors
class bgcolors:
    black = '\033[40m'
    reset = '\033[0m'

# Function to print the board
def print_board():
    global board

    render_board = board.copy()

    for i in range(0, 9):
        if render_board[i] == " ":
            render_board[i] = i
        elif render_board[i] == "X":
            render_board[i] = colors.red + render_board[i] + colors.reset
        elif render_board[i] == "O":
            render_board[i] = colors.blue + render_board[i] + colors.reset

    if current_player == "X":
        print(f'{bgcolors.black}{colors.white} Player: {colors.red}X {bgcolors.reset}')
    else:
        print(f'{bgcolors.black}{colors.white} Player: {colors.blue}O {bgcolors.reset}')
    print(f'{bgcolors.black}{colors.white} Turn  : {turn} {bgcolors.reset}')

    print('┌─────┬─────┬─────┐')
    print(f'│  {render_board[0]}  │  {render_board[1]}  │  {render_board[2]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {render_board[3]}  │  {render_board[4]}  │  {render_board[5]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {render_board[6]}  │  {render_board[7]}  │  {render_board[8]}  │')
    print('└─────┴─────┴─────┘')

# Ask the player to choose x or o
def choose_player():
    global current_player
    player = input("Choose X or O: ")
    if player == "X":
        current_player = "X"
    elif player == "O":
        current_player = "O"
    else:
        print("Invalid input")
        choose_player()

# Make a function to check if the game is over
def check_game_over():
    global board
    global turn
    if turn == 9:
        return True
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

# Function to get the player input
def get_player_input():
    global board
    global current_player
    global turn

    player_input = input(f"{colors.green}It's your turn! Choose a number on the board!\n>>> {colors.reset}")

    try:
        player_input = int(player_input)
    except:
        print("Invalid input")
        get_player_input()
        return
    if player_input < 0 or player_input > 8:
        print("Invalid input")
        get_player_input()
        return
    if board[player_input] != " ":
        print("Invalid input")
        get_player_input()
        return
    board[player_input] = current_player
    turn += 1
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Function to make the computer play
def computer_play():
    global board
    global current_player
    global turn

    # Check for winning move
    for i in range(0, 9):
        if board[i] == " ":
            board[i] = current_player
            if check_game_over():
                computer_select(i)
                return
            board[i] = " "

    # Check for blocking move
    if current_player == "X":
        other_player = "O"
    else:
        other_player = "X"

    for i in range(0, 9):
        if board[i] == " ":
            board[i] = other_player
            if check_game_over():
                computer_select(i)
                return
            board[i] = " "

    # Check for center
    if board[4] == " ":
        computer_select(4)
        return

    # Check for connecting move
    for i in range(0, 9):
        if board[i] == " ":
            board[i] = current_player
            for j in range(0, 9):
                if board[j] == " ":
                    board[j] = current_player
                    if check_game_over():
                        computer_select(i)
                        return
                    board[j] = " "
            board[i] = " "

    # Random move
    empty_spaces = []
    for i in range(0, 9):
        if board[i] == " ":
            empty_spaces.append(i)

    computer_select(random.choice(empty_spaces))


def computer_select(grid):
    global turn
    print(f'{colors.red}Compter choose {grid} as their move!{colors.reset}')
    board[grid] = current_player
    turn += 1


# Function to play the game
def play_game():
    global board
    global current_player
    global turn
    while True:
        print_board()
        get_player_input()
        if turn == 9:
            print("="*40)
            print(f"{colors.yellow}Game over! It's a tie!{colors.reset}")
            print_board()
            print("=" * 40)
            break
        if check_game_over():
            print("=" * 40)
            print(f"{colors.yellow}Game over! You won!{colors.reset}")
            print_board()
            print("=" * 40)
            break

        computer_play()
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        if check_game_over():
            print("=" * 40)
            print(f"{colors.yellow}Game over! You lost!{colors.reset}")
            print_board()
            print("=" * 40)
            break

# Function to reset the game
def reset_game():
    global board
    global current_player
    global turn
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    turn = 0


def play():
    reset_game()
    choose_player()
    play_game()

    replay = input("Do you want to play again? (y/n) ")
    if replay == "y":
        play()
    else:
        print("Thanks for playing!")
        exit(0)

play()