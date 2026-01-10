import qrcode
from datetime import datetime

# https://pypi.org/project/qrcode/

# version 2.0

SINGLE = "a"
MULTIPLE = "b"

read_only_list = (SINGLE, MULTIPLE)

def print_qr_code_single():
    user_input = input("Enter text or URL to generate QR Code: ")
    user_file_name = input("Enter the filename: ")
    img = qrcode.make(user_input)
    img.save(f"img/{user_file_name}.png")
    print(f"Done generating {user_file_name}.png")

def print_qr_code_multiple():
    multiple_user_input = []
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d%H%M%S")
    user_input = input("Enter list of text or URL separated by comma: ")
    multiple_user_input = [item.strip() for item in user_input.split(",")]
    for i in range(len(multiple_user_input)):
        img = qrcode.make(multiple_user_input[i])
        img.save(f"img/{formatted_date}_{i+1}.png")
        print(f"Done generating {formatted_date}_{i+1}.png")

def single_or_multiple():
    while True:
        print()
        print("You want to generate single or multiple QR Code?")
        print("Option A - single QR Code")
        print("Option B - multiple QR Code")
        user_input = input("Please enter A or B: ").lower()
        if user_input in read_only_list:
            return user_input
        print("Invalid input!")

def start_task():
    user_input = single_or_multiple()
    if (user_input == SINGLE):
        print_qr_code_single()
    else:
        print_qr_code_multiple()

start_task()