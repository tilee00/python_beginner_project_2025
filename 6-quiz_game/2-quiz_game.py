from 2-quiz_game_constants import OPERATION_EDIT_QUIZ

def print_operation():
    print("""
        Please choose the operation that you want (1-5):
        1) Start quiz game
        2) Import quiz questions
        3) View all quiz questions
        4) Edit quiz question
        5) Exit
    """)

def main():
    print_operation()
    print(OPERATION_EDIT_QUIZ)

main()