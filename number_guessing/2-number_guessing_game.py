import random
import sys

# version 2.0

count_of_attempts = 5
count_of_game = 0
best_score = 0

def setBestScore(score):
    if (count_of_game == 0):
        score = 5-count_of_attempts
        return score
    if ((5-count_of_attempts) < score):
        score = 5-count_of_attempts
        return score
    
def setCountOfGame(count):
    print(f"ROUND {count + 2} of the game starts: ")
    count += 1
    return count

def exitProgram(input):
    if(input.lower() == "exit"):
        print()
        print(f"Thanks for playing! Your highest score is {best_score}")
        sys.exit()

print("Welcome to number guessing game! Enter exit to end the game at any time. ")

while True:
    try:
        min_num = input("Please enter the minimum number for guessing: ")
        exitProgram(min_num)
        min_num = int(min_num)
        break
    except ValueError:
        print("Please enter a valid number")
while True:
    try:
        while(True):
            max_num = input("Please enter the maximum number for guessing: ")
            exitProgram(max_num)
            max_num = int(max_num)

            if(max_num > min_num):
                break
            else:
                print("Maximum number must be greater than minimum number")
        break
    except ValueError:
        print("Please enter a valid number")

random_num = random.randint(min_num, max_num)

print()
print("The game is ready. Starting now.")
print()

while True:
    try:
        while(True):
            if(count_of_attempts > 0):
                print(f"You have {count_of_attempts} attempts left")
                user_input = input(f"Guess the number between {min_num} and {max_num}: ")
                count_of_attempts -=1

                exitProgram(user_input)
                user_input = int(user_input)

                if(user_input <= 0 and user_input > 100):
                    print("Please enter a valid number")
                elif(user_input == random_num):
                    print(f"Congratulations! You guessed the number ({random_num}).")
                    best_score = setBestScore(best_score)
                    count_of_attempts = 5
                    print()
                    count_of_game = setCountOfGame(count_of_game)
                    break
                elif (user_input < min_num or user_input > max_num):
                    print("Out of range!")
                elif (user_input < random_num): 
                    print("Too Low!")
                else:
                    print("Too High!")
            else:
                print(f"You have run out of attempts. Game over. The answer is {random_num}")
                best_score = setBestScore(best_score)
                count_of_attempts = 5
                print()
                count_of_game = setCountOfGame()
                break

    except ValueError:
        print("Please enter a valid number")

    