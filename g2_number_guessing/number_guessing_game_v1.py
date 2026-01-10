import random

# version 1.0

random_num = random.randint(1,100)

while True:
    try:
        user_input = int(input("Guess the number between 1 and 100: "))

        if(user_input <= 0 and user_input > 100):
            print("Please enter a valid number")
        elif(user_input == random_num):
            print("Congratulations! You guessed the number.")
            break
        elif (user_input < random_num):
            print("Too Low!")
        else:
            print("Too High!")

    except ValueError:
        print("Please enter a valid number")
    