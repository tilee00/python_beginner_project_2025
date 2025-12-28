from enum import Enum
import random

# declare constant for r/p/s
# ROCK = "r"; SCISSOR = "s"; PAPER = "p";
# a better way is to use Key-Value Mapping
# emojis = {ROCK: "🪨", SCISSOR:"✂️", PAPER:"📃"}
class RockPaperScissor(Enum):
    ROCK = (1,"r","🪨")
    PAPER = (2,"p","📃")
    SCISSOR = (3,"s","✂️")

    def __init__(self, int_value, str_value, icon):
        self.int_value = int_value
        self.str_value = str_value
        self.icon = icon

# function name should use snake_case get_icon_by_int(num)
def getIconByInt(num):
    if(num == 1):
        return RockPaperScissor.ROCK.icon
    elif(num == 2):
        return RockPaperScissor.PAPER.icon
    else:
        return RockPaperScissor.SCISSOR.icon
    
def getIconByStr(input):
    if(input == "r"):
        return RockPaperScissor.ROCK.icon
    elif(input == "p"):
        return RockPaperScissor.PAPER.icon
    else:
        return RockPaperScissor.SCISSOR.icon

# a better way is simply getResult to 
# if(same choice) then "It's a tie!"
# if(win condition) then "You win"
# else "You lose"
# NOTE: Use a backslash '\' or parenthesis '()' to continue an expression across multiple lines
def getResult(user_icon, computer_icon):
    if(user_icon == RockPaperScissor.ROCK.icon):
        # if user is rock
        if(computer_icon == RockPaperScissor.ROCK.icon):
            return "It's a tie!"
        elif(computer_icon == RockPaperScissor.PAPER.icon):
            return "You lose"
        else:
            return "You win"

    elif (user_icon == RockPaperScissor.PAPER.icon):
        # if user is paper
        if(computer_icon == RockPaperScissor.PAPER.icon):
            return "It's a tie!"
        elif(computer_icon == RockPaperScissor.SCISSOR.icon):
            return "You lose"
        else:
            return "You win"

    else:
        # if user is scissor
        if(computer_icon == RockPaperScissor.SCISSOR.icon):
            return "It's a tie!"
        elif(computer_icon == RockPaperScissor.ROCK.icon):
            return "You lose"
        else:
            return "You win"

game_count = 0

# The code can be improved by modularizing the large code into smaller functions.
# NOTE (Don't Repeat Yourself) Avoid repeating r/p/s declarations; it can lead to typos and make changes harder.
while (True):
    # a better way is to use computer_choice = random.choice(read_only_choices)
    computer_int_choice = random.randint(1,3)
    user_input = input("Rock🪨, paper📃 or scissors✂️? (r/p/s): ").lower()

    # a better way is to use for loop + tuple list
    # read_only_choices = ("r", "p", "s") or read_only_choices = tuple(emojis.keys())
    # if user_input not in read_only_choices: print("invalid_message"); continue;
    if(user_input != "r" and user_input != "p" and user_input != "s"):
        print("Invalid choice!")
    else:
        computer_icon_choice = getIconByInt(computer_int_choice)
        user_icon_choice = getIconByStr(user_input)
        # if using key-value Mapping, then can get user icon 
        # by emojis[user_input] and emojis[computer_choice]
        print(f"You chose {user_icon_choice}")
        print(f"Computer chose {computer_icon_choice}")

        result = getResult(user_icon_choice, computer_icon_choice)
        print(result)
        game_count+=1

        isCountinue = input("Countinue? (y/n): ").lower()

        while(True):
            if (isCountinue == "n" or isCountinue == "y"):
                break
            else:
                print("Invalid input")

        if(isCountinue == "n"):
            print("Thanks for playing")
            break

        if(isCountinue == "y"):
            print()
            print(f"Round {game_count+1} Start")
    