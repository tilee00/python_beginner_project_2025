from data.quiz_game_constants_v2 import (
    EDIT_QUESTION,
    ENTER_NEW_QUESTION,
    QUESTION_CONFIRM_REPLACE,
    ANSWER_YES,
    EDITION_SUCCESS,
    EDITION_RESET_ONCE_LEAVE,
    INVALID_ERROR_SHOULD_BE_ABC,
    INVALID_ERROR_SHOULD_BE_12,
    INVALID_ERROR_SHOULD_BE_YN,
    option_list,
    should_continue_list,
)
from .quiz_game_shared_operation_v2 import (
    print_quiz_difficulty,
    should_continue,
    quiz_game,
)


def get_no_of_question():
    while True:
        try:
            no_of_question = int(input(EDIT_QUESTION))
            if no_of_question <= 0:
                raise ValueError
            else:
                if no_of_question in (1, 2):
                    return no_of_question
                else:
                    raise ValueError
        except ValueError:
            print(INVALID_ERROR_SHOULD_BE_12)


def get_new_question():
    print(ENTER_NEW_QUESTION)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def get_new_answer():
    while True:
        new_answer = input("Enter the answer of your quesiton (a/b/c): ").upper()
        if new_answer in option_list:
            return new_answer
        print(INVALID_ERROR_SHOULD_BE_ABC)


def view_new_question(
    new_question, new_answer, no_of_question, question_list, difficulty
):
    print()
    print("-------------The old question-------------")
    old_question_key = list(question_list[difficulty].keys())[no_of_question - 1]
    print(old_question_key)
    print("The answer: ", end="")
    print(question_list[difficulty][old_question_key])
    print()
    print("-------------The new question-------------")
    print(new_question)
    print("The answer: ", end="")
    print(new_answer)


def confirm_new_question(
    new_question, new_answer, no_of_question, category_data, difficulty, full_data
):
    while True:
        user_input = input(QUESTION_CONFIRM_REPLACE).upper()
        if user_input in should_continue_list:
            if user_input == ANSWER_YES:
                # 1. Identify the old key
                keys_list = list(category_data[str(difficulty)].keys())
                old_key = keys_list[no_of_question - 1]

                # 2. Remove old and add new
                del category_data[str(difficulty)][old_key]
                category_data[str(difficulty)][new_question] = new_answer

                # 3. Save the entire updated structure to the JSON file
                save_quiz_data(full_data)

                print(EDITION_SUCCESS)
                print("--- Changes saved permanently to JSON ---")
                break
            else:
                break
        else:
            print(INVALID_ERROR_SHOULD_BE_YN)


def edit_question(question_list, difficulty):
    no_of_question = get_no_of_question()
    new_question = get_new_question()
    new_answer = get_new_answer()
    view_new_question(
        new_question, new_answer, no_of_question, question_list, difficulty
    )
    confirm_new_question(
        new_question, new_answer, no_of_question, question_list, difficulty
    )


def quiz(question_list, action):
    difficulty = print_quiz_difficulty()
    edit_question(question_list, difficulty)
    should_continue()


def edit_quiz_game():
    quiz_game(quiz, None)


if __name__ == "__quiz_game_operation_v2__":
    edit_quiz_game()
