from data.quiz_game_constants_v2 import QUIZ_CATEGORIES, DIFFICULTY_LEVEL, option_list, math_question, tech_question, science_question

def print_start_quiz():
    while True:
        try:
            return int(input(QUIZ_CATEGORIES))
        except:
            print("Invalid option. Try a number between 1 and 4")

def print_quiz_difficulty():
    while True:
        try:
            return int(input(DIFFICULTY_LEVEL))
        except:
            print("Invalid option. Try a number between 1 and 4")
            
def print_question(list, difficulty):
    for question in list[difficulty]:
        print(question)
        math_answer = validate_answer()
        evaluate_answer(math_answer, list[difficulty][question])
    
def validate_answer():
    while True:    
        user_input = input("Enter your choice: ").upper()
        if user_input in option_list:
            return user_input
        print("Invalid option. Please enter a, b or c.")
        
def evaluate_answer(user_answer, standard_answer):
    if (user_answer == standard_answer):
        print("Correct answer!")
    else:
        print("Wrong answer!")
    
def math_quiz():
    difficulty = print_quiz_difficulty()
    print_question(math_question, difficulty)
    
def technology_quiz():
    difficulty = print_quiz_difficulty()
    print_question(tech_question, difficulty)
    
def science_quiz():
    difficulty = print_quiz_difficulty()
    print_question(science_question, difficulty)
    
def operation_back_to_main():
    from operation.quiz_game_operation_v2 import main_operation
    main_operation()

def start_quiz_game():
    user_option = print_start_quiz()
    match user_option:
        case 1:
            math_quiz()
        case 2:
            technology_quiz()
        case 3:
            science_quiz()
        case 4:
            operation_back_to_main()
        case _:
            print("Invalid option. Try a number between 1 and 4")

if __name__ == "__quiz_game_operation_v2__":
    start_quiz_game()