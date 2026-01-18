import json
import os
from data.quiz_game_constants_v2 import (
    QUIZ_CATEGORIES,
    DIFFICULTY_LEVEL,
    ANSWER_YES,
    THANK_YOU,
    INVALID_ERROR_SHOULD_BE_ABC,
    INVALID_ERROR_SHOULD_BE_1234,
    INVALID_ERROR_SHOULD_BE_YN,
    option_list,
    should_continue_list,
    math_question,
    tech_question,
    science_question,
)

DATA_FILE = "data.quiz_data.json"


def load_quiz_data():
    if os.path.exists(DATA_FILE):
        # "r" = read
        # with keyword will auto close the file after finish task
        with open(DATA_FILE, "r") as file:
            # json.load = translate json file into python dictionary
            return json.load(file)
    else:
        # Fallback if file doesn't exist
        print("Data file not exist")
        return {"math": {}, "tech": {}, "science": {}}


def save_quiz_data(data):
    # "w" = write, deletes everything currently in the file and starts fresh
    # "a" = append, add new data at the very end without delete
    with open(DATA_FILE, "w") as file:
        # translate python dictionary to text
        json.dump(data, file, indent=4)


def print_start_quiz():
    while True:
        try:
            return int(input(QUIZ_CATEGORIES))
        except:
            print(INVALID_ERROR_SHOULD_BE_1234)


def print_quiz_difficulty():
    while True:
        try:
            return int(input(DIFFICULTY_LEVEL))
        except:
            print(INVALID_ERROR_SHOULD_BE_1234)


def print_and_evaluate_question(question_list, difficulty):
    for question in question_list[difficulty]:
        print(question)
        math_answer = validate_answer()
        evaluate_answer(math_answer, question_list[difficulty][question])


def print_and_view_question(question_list, difficulty):
    for question in question_list[difficulty]:
        print(question)


def validate_answer():
    while True:
        user_input = input("Enter your choice: ").upper()
        if user_input in option_list:
            return user_input
        print(INVALID_ERROR_SHOULD_BE_ABC)


def evaluate_answer(user_answer, standard_answer):
    if user_answer == standard_answer:
        print("Correct answer!")
    else:
        print("Wrong answer!")


def should_continue():
    while True:
        user_input = input("Do you want to continue? (y/n): ").upper()
        if user_input in should_continue_list:
            if user_input == ANSWER_YES:
                return operation_back_to_main()
            else:
                print(THANK_YOU)
                break
        print(INVALID_ERROR_SHOULD_BE_YN)


def operation_back_to_main():
    from operation.quiz_game_operation_v2 import main_operation

    main_operation()


def quiz(question_type, action):
    difficulty = print_quiz_difficulty()
    action(question_type, difficulty)
    should_continue()


def quiz_game(quiz, action):
    all_data = load_quiz_data()
    user_option = print_start_quiz()

    category_map = {1: "math_question", 2: "tech_question", 3: "science_question"}
    
    if user_option in category_map:
        category_key = category_map[user_option]
        # Pass the specific category data to the logic function
        quiz(all_data[category_key], action)
    elif user_option == 4:
        operation_back_to_main()
    else:
        print(INVALID_ERROR_SHOULD_BE_1234)
