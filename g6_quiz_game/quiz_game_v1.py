
QUESTION_ONE = 0
QUESTION_TWO = 1

OPTION_A = "a"
OPTION_B = "b"
OPTION_C = "c"

option_list = (OPTION_A, OPTION_B, OPTION_C)

questions_answer = {
    QUESTION_ONE : OPTION_B, 
    QUESTION_TWO : OPTION_C
}

def question_1():
    print("What is the result of 3+19?")
    print("a) 21")
    print("b) 22")
    print("c) 23")

def question_2():
    print("What is the result of 9+28?")
    print("a) 35")
    print("b) 32")
    print("c) 37")

def get_question(number_of_questions):
    match number_of_questions:
        case 0:
            question_1()
        case 1:
            question_2()
        case _:
            print("Error happened.")

def display_question(number_of_questions):
    print()
    print(f"Question {number_of_questions + 1}: ", end='')
    get_question(number_of_questions)

def evaluate_answer(number_of_questions, correct):
    while True:
        answer = input("Your answer: ").lower()
        if answer in option_list:
            if answer == questions_answer[number_of_questions]:
                correct += 1
                print("Correct!")
            else:
                print("Wrong!")
            return correct
        else:
            print("Please enter a, b or c.")
        
def print_final_score(number_of_questions, correct):
    print()
    print(f"Your final score: {correct}/{number_of_questions}")

def main():
    number_of_questions = 2
    correct = 0
    for i in range(number_of_questions):
        display_question(i)
        correct = evaluate_answer(i, correct)
    
    print_final_score(number_of_questions, correct)

main()