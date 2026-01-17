from g6_quiz_game.quiz_game_v2.data.quiz_game_constants_v2 import *
import sys

def print_operation():
    while True:
        try:
            return int(input("""
                Please choose the operation that you want (1-5):
                1) Start quiz game
                2) Import quiz questions
                3) View all quiz questions
                4) Edit quiz question
                5) Exit
            """))
        except:
            print("Invalid option. Try a number between 1 and 5")

def operation_start_quiz():
    print("operation 1")
    
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

def enter_operation():
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

if __name__ == "__quiz_game_main_v2__":
    enter_operation()