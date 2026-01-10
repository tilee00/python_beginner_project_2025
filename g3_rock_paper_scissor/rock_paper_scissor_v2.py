import random

ROCK = "r"
SCISSOR = "s"
PAPER = "p"
YES = "y"
NO = "n"
EXIT = "exit"
ONE = 1
TWO = 2
COMPUTER_USERNAME = "Computer"

standard_choice = {ROCK : "🪨", SCISSOR : "✂️", PAPER : "📃"}
should_continue_list = (YES, NO)
num_of_players = (ONE, TWO)
standard_list = tuple(standard_choice.keys())

user_score = 0
computer_score = 0
tie_score = 0

player1_name = ""
player2_name = ""

def should_exit(input):
    if(input == EXIT):
        print("Thanks for playing")
        exit()

def start_message():
    while True:
        print()
        print("Enter exit to end the game at any time")
        user_input = input("Scissor Paper Rock! 1 Player or 2 Players? (1/2): ")
        should_exit(user_input)
        try:
            if int(user_input) in num_of_players:
                return int(user_input)
        except:
            print("Invalid input")
        print("Please choose a number between 1 and 2")

def get_players_name(num_of_players):
    global player1_name
    global player2_name
    players_name_list = []

    for i in range(num_of_players):
        user_input = input(f"Hi Player {i+1}, Please enter your username: ")
        should_exit(user_input)
        players_name_list.append(user_input)

    if (num_of_players == ONE):
        players_name_list.append(COMPUTER_USERNAME)

    player1_name, player2_name = players_name_list

def input_validation_check():
    while True:
        user_input = input("Rock🪨, paper📃 or scissors✂️? (r/p/s): ").lower()
        should_exit(user_input)
        if user_input in standard_list:
            return user_input        
        print("Invalid choice!")

def get_user_input(num_of_round, num_of_players):
    global player1_name
    global player2_name
    players_input = []
    for i in range(num_of_players):
        print()
        print(f"Player {i+1}: ")
        print(f"Scissor Paper Rock - Round {num_of_round+1}: ")
        user_input = input_validation_check()
        players_input.append(user_input)

    if(num_of_players == ONE):    
        computer_choice = random.choice(standard_list)
        players_input.append(computer_choice)
    
    return players_input

def print_choices(user_input, computer_choice):
    print(f"You chose {standard_choice[user_input]}")
    print(f"Computer chose {standard_choice[computer_choice]}")

def print_choices_2_players(player1_input, player2_input):
    print(f"Player 1 chose {standard_choice[player1_input]}")
    print(f"Player 2 chose {standard_choice[player2_input]}")

# get_result can also define a key-Value Mapping
# example: win when user is ROCK, computer is scissor
# WIN_RULES = {
#     ROCK: SCISSOR,
#     SCISSOR: PAPER,
#     PAPER: ROCK
# }
# elif WIN_RULES[user] == computer:
def get_result(player1, player2):
    global player1_name, player2_name
    global user_score, computer_score, tie_score
    print()
    if(player1 == player2):
        print("It's a tie!")
        tie_score += 1
    elif(
        (player1 == ROCK and player2 == SCISSOR) or
        (player1 == SCISSOR and player2 == PAPER) or
        (player1 == PAPER and player2 == ROCK)
    ):
        print(f"Player 1 ({player1_name}) win")
        print(f"Player 2 ({player2_name}) lose")
        user_score += 1
    else:
        print(f"Player 1 ({player1_name}) lose")
        print(f"Player 2 ({player2_name}) win")
        computer_score += 1

def print_overall_winner(num_of_players):
    global user_score, computer_score, tie_score, player1_name, player2_name
    print()
    print("Game Over!")
    print(f"Player 1 ({player1_name}) score is {user_score}")
    print(f"Player 2 ({player2_name}) score is {computer_score}")
    print(f"Tie score is {tie_score}")
    print()
    if (user_score > tie_score and user_score > computer_score):
        print(f"Winner is player 1 ({player1_name})!")
    elif (computer_score > tie_score and computer_score > user_score):
        print(f"Winner is player 2 ({player2_name})!")
    else:
        print("No winner. Both drew")

def single_player():
    num_of_round = 0
    global player1_name
    global player2_name
    get_players_name(ONE)
    while True:
        user_input, computer_choice = get_user_input(num_of_round, ONE)
        print_choices(user_input, computer_choice)
        get_result(user_input, computer_choice)
        num_of_round += 1
        if(num_of_round == 3):
            print_overall_winner(ONE)
            break

def two_players():
    num_of_round = 0
    global player1_name
    global player2_name
    get_players_name(TWO)
    while True:
        player1_input, player2_input = get_user_input(num_of_round, TWO)
        print_choices_2_players(player1_input, player2_input)
        get_result(player1_input, player2_input)
        num_of_round += 1
        if(num_of_round == 3):
            print_overall_winner(TWO)
            break

def start_game():
    user_input = start_message()
    if(user_input == ONE):
        single_player()
    else:
        two_players()

start_game()
