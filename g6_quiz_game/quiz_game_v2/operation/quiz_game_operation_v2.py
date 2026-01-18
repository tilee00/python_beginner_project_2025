import sys
from .quiz_game_operation_edit_quiz_v2 import edit_quiz_game
from data.quiz_game_constants_v2 import (
    MAIN_MENU,
    THANK_YOU,
    INVALID_ERROR_SHOULD_BE_1TO5,
)
from .quiz_game_shared_operation_v2 import (
    quiz,
    print_and_evaluate_question,
    print_and_view_question,
    quiz_game,
)


def print_operation():
    while True:
        try:
            return int(input(MAIN_MENU))
        except:
            print(INVALID_ERROR_SHOULD_BE_1TO5)


def operation_start_quiz():
    quiz_game(quiz, print_and_evaluate_question)


def operation_import_quiz():
    print("operation import")


def operation_view_quiz():
    quiz_game(quiz, print_and_view_question)


def operation_edit_quiz():
    edit_quiz_game()


def operation_exit():
    print()
    print(THANK_YOU)
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
            print(INVALID_ERROR_SHOULD_BE_1TO5)
