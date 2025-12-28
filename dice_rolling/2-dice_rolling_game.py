import random

count = 0
def getUserInput():
    return input("Roll the dice? (y/n): ")

while(True):
    user_input = getUserInput().lower()
    if(user_input == "n"):
        print(f"Thanks for playing! You rolled {count} times in this session.")
        break

    elif(user_input == "y"):

        while(True):
            input_dices = input("How many dice you want to roll? (maximum 3): ")
            try:
                num_of_dices = int(input_dices)
                if(num_of_dices <= 0 or num_of_dices > 3):
                    print("Invalid number! Please choose a number between 1 and 3.")
                else:
                    count += 1
                    for num in range(num_of_dices):
                        result = random.randint(1, 6)
                        print(f"(Dice {num+1} rolled a {result})")
                    break        
            except ValueError:
                print("Invalid number! Please choose a number between 1 and 3.")    

    else:
        print("Invalid choice!")