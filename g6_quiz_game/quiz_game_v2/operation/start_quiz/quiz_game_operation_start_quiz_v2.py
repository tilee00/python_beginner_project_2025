from data.quiz_game_constants_v2 import *
import sys

def print_start_quiz():
    while True:
        try:
            return int(input("""
Please choose the quiz categories that you want (1-3):
1) Math
2) Technology
3) Sciece
4) Back to main menu
Enter your choice: """))
        except:
            print("Invalid option. Try a number between 1 and 4")

def print_quiz_difficulty():
    while True:
        try:
            return int(input("""
Please choose the quiz difficulty level that you want (1-3):
1) Easy
2) Medium
3) Hard
4) Back to quiz categories
Enter your choice: """))
        except:
            print("Invalid option. Try a number between 1 and 4")
    
def math_quiz(difficulty):
    match difficulty:
        case 1:
            easy_math_quiz()
        case 2:
            medium_math_quiz()
        case 3:
            hard_math_quiz()
        case 4:
            start_quiz_game()
    
def easy_math_quiz():
    print("operation easy math")
    
def medium_math_quiz():
    print("operation medium_math_quiz")
    
def hard_math_quiz():
    print("operation hard_math_quiz")
    
def technology_quiz(difficulty):
    print("operation tech")
    
def science_quiz(difficulty):
    print("operation science")
    
def operation_back_to_main():
    from operation.quiz_game_operation_v2 import main_operation
    main_operation()

def start_quiz_game():
    user_option = print_start_quiz()
    match user_option:
        case 1:
            difficulty = print_quiz_difficulty()
            math_quiz(difficulty)
        case 2:
            difficulty = print_quiz_difficulty()
            technology_quiz(difficulty)
        case 3:
            difficulty = print_quiz_difficulty()
            science_quiz(difficulty)
        case 4:
            operation_back_to_main()
        case _:
            print("Invalid option. Try a number between 1 and 4")

if __name__ == "__quiz_game_operation_v2__":
    start_quiz_game()