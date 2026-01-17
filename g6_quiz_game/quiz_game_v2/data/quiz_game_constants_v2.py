MAIN_MENU = """
===================MAIN MENU===================
Please choose the operation that you want (1-5):
1) Start quiz game
2) Import quiz questions
3) View all quiz questions
4) Edit quiz question
5) Exit
Enter your choice: """

QUIZ_CATEGORIES = """
Please choose the quiz categories that you want (1-3):
1) Math
2) Technology
3) Sciece
4) Back to main menu
Enter your choice: """

DIFFICULTY_LEVEL = """
Please choose the quiz difficulty level that you want (1-3):
1) Easy
2) Medium
3) Hard
4) Back to quiz categories
Enter your choice: """

ANSWER_A = "A"
ANSWER_B = "B"
ANSWER_C = "C"

option_list = (ANSWER_A, ANSWER_B, ANSWER_C)

# MATH
EASY_MATH_QUESTION_1 = """
1 - What is the result of 3+5?
a) 8
b) 7
c) 9
"""
EASY_MATH_QUESTION_2 = """
2 - What is the result of 1+9?
a) 9
b) 10
c) 11
"""
MEDIUM_MATH_QUESTION_1 = """
1 - What is the result of 100/4*12?
a) 200
b) 25
c) 300
"""
MEDIUM_MATH_QUESTION_2 = """
2 - What is the square root of 256?
a) 16
b) 8
c) 18
"""
HARD_MATH_QUESTION_1 = """
1 - if 3x² + 5x = 24x + 14, What is the value of x? 
a) 7
b) 6
c) 8
"""
HARD_MATH_QUESTION_2 = """
2 - if 4/a = a/16, What is the value of a?
a) 2
b) 4
c) 8
"""

# TECH
EASY_TECH_QUESTION_1 = """
1 - 'OS' computer abbreviation usually means?
a) Open Software
b) Operating System
c) Optical Sensor
"""
EASY_TECH_QUESTION_2 = """
2 - '.MOV' extension refers usually to what kind of file?
a) Audio file
b) Animation/movie file
c) MS Office document
"""
MEDIUM_TECH_QUESTION_1 = """
1 - How many bits is a byte?
a) 16
b) 8
c) 4
"""
MEDIUM_TECH_QUESTION_2 = """
2 - What do you call a computer on a network that requests files from another computer?
a) A client
b) A host
c) A web server
"""
HARD_TECH_QUESTION_1 = """
1 - Which was an early mainframe computer?
a) ENIAC
b) BRAINIA
c) UNIC
"""
HARD_TECH_QUESTION_2 = """
2 - Which of the following operating systems is produced by IBM?
a) UNIX
b) Windows
c) OS-2
"""

# SCIENCE
EASY_SCIENCE_QUESTION_1 = """
1 - Which planet is closest to the sun?
a) Moon
b) Mars
c) Mercury
"""
EASY_SCIENCE_QUESTION_2 = """
2 - Pollination is best defined as
a) transfer of pollen from anther to stigma
b) germination of pollen grains
c) visiting flowers by insects
"""
MEDIUM_SCIENCE_QUESTION_1 = """
1 - Movement of cell against concentration gradient is called
a) passive transport
b) active transport
c) osmosis
"""
MEDIUM_SCIENCE_QUESTION_2 = """
2 - What is the smallest unit of matter?
a) atom
b) protons
c) electrons
"""
HARD_SCIENCE_QUESTION_1 = """
1 - Plants synthesis protein from
a) starch
b) sugar
c) amino acids
"""
HARD_SCIENCE_QUESTION_2 = """
2 - One of the following is not a function of bones.
a) Secretion of hormones for calcium regulation in blood and bones
b) Production of blood corpuscles
c) Place for muscle attachment
"""

math_question = {
    1 : {
        EASY_MATH_QUESTION_1 : ANSWER_A,
        EASY_MATH_QUESTION_2 : ANSWER_B,
    },
    2: {
        MEDIUM_MATH_QUESTION_1 : ANSWER_C,
        MEDIUM_MATH_QUESTION_2 : ANSWER_A,
    },
    3: {
        HARD_MATH_QUESTION_1 : ANSWER_A,
        HARD_MATH_QUESTION_2 : ANSWER_C,
    }
}

tech_question = {
    1 : {
        EASY_TECH_QUESTION_1 : ANSWER_B,
        EASY_TECH_QUESTION_2 : ANSWER_B,
    },
    2: {
        MEDIUM_TECH_QUESTION_1 : ANSWER_B,
        MEDIUM_TECH_QUESTION_2 : ANSWER_A,
    },
    3: {
        HARD_TECH_QUESTION_1 : ANSWER_A,
        HARD_TECH_QUESTION_2 : ANSWER_C,
    }
}

science_question = {
    1 : {
        EASY_SCIENCE_QUESTION_1 : ANSWER_C,
        EASY_SCIENCE_QUESTION_2 : ANSWER_A,
    },
    2: {
        MEDIUM_SCIENCE_QUESTION_1 : ANSWER_B,
        MEDIUM_SCIENCE_QUESTION_2 : ANSWER_A,
    },
    3: {
        HARD_SCIENCE_QUESTION_1 : ANSWER_C,
        HARD_SCIENCE_QUESTION_2 : ANSWER_A,
    }
}