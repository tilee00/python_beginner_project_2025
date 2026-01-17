from data.quiz_game_constants_v2 import *
from operation.start_quiz.quiz_game_operation_start_quiz_v2 import start_quiz_game
import sys

def print_operation():
    while True:
        try:
            return int(input("""
===================MAIN MENU===================
Please choose the operation that you want (1-5):
1) Start quiz game
2) Import quiz questions
3) View all quiz questions
4) Edit quiz question
5) Exit
Enter your choice: """))
        except:
            print("Invalid option. Try a number between 1 and 5")

def operation_start_quiz():
    start_quiz_game()
    
def operation_import_quiz():
    print("operation 2")
    
def operation_view_quiz():
    print("operation 2")
    
def operation_edit_quiz():
    print("operation 2")
    
def operation_exit():
    print()
    print(f"Thanks for playing!")
    sys.exit()

def main_operation():
    user_option = print_operation()
    match user_option:
        case 1:
            operation_start_quiz()
        case 2:
            operation_import_quiz()
        case 3:
            operation_view_quiz()
        case 4:
            operation_edit_quiz()
        case 5:
            operation_exit()
        case _:
            print("Invalid option. Try a number between 1 and 5")


main_operation()