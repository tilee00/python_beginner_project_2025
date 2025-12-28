

# version 1.0

# SGD, MYR, JPY
# 1 SGD = 3.15 MYR
# 1 JPY = 0.026 MYR

def validate_input_amount():
    while True:
        try:
            input_amount = float(input("Enter the amount: "))
            return input_amount
        except:
            print("Please enter a valid amount")

def start_convert():
    validate_input_amount()
    

start_convert()