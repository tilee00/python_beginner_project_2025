import random

def getUserInput():
    return input("Roll the dice? (y/n): ")

while(True):
    user_input = getUserInput().lower()
    if(user_input == "n"):
        print("Thanks for playing!")
        break
    elif(user_input == "y"):
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        print(f"({first_num}, {second_num})")
    else:
        print("Invalid choice!")