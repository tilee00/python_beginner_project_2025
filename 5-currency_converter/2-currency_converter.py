

# version 2.0

# 1 SGD = 3.15 MYR
# 1 SGD = 122 JPY
# 1 JPY = 0.026 MYR
# 1 JPY = 0.0082 SGD
# 1 MYR = 0.32 SGD
# 1 MYR = 39 JPY

SGD = "SGD" # Singapore
JPY = "JPY" # Japan
MYR = "MYR" # Malaysia
CNY = "CNY" # China
USD = "USD" # United States of America
SOURCE = "Source"
TARGET = "Target"
YES = "y"
NO = "n"

should_continue_list = (YES, NO)

type_list = {
    SGD: {
        JPY: 121.9577,
        MYR: 3.1535,
        CNY: 5.4397,
        USD: 0.7778
    },
    JPY: {
        SGD: 0.0082,
        MYR: 0.0259,
        CNY: 0.0446,
        USD: 0.0064
    },
    MYR : {
        SGD: 0.3171,
        JPY: 38.6734,
        CNY: 1.7245,
        USD: 0.2466
    },
    CNY : {
        SGD: 0.1838,
        JPY: 22.4190,
        MYR: 0.5799,
        USD: 0.1430
    },
    USD : {
        SGD: 1.2857,
        JPY: 156.7950,
        MYR: 4.0555,
        CNY: 6.9939
    }
}

def validate_input_amount():
    while True:
        try:
            input_amount = float(input("Enter the amount: "))
            return input_amount
        except:
            print("Please enter a valid amount")

def choose_source(type, source):
    while True:
        input_type = input(f"{type} currency (SGD, JPY, MYR, CNY, USD): ").upper()
        
        if(input_type in type_list):
            return input_type.upper()
        
        print("Invalid currency. Please use SGD, JPY, MYR, CNY or USD.")

def get_num_of_target():
    while True:
        try:
            print("====")
            input_num = int(input("How many currencies would you like to convert to? (1-4): "))
            print("====")
        except:
            print("Please enter a number from 1 to 4.")
            continue

        if (input_num >= 1 and input_num <= 4):
            return input_num
        
        print("Please enter a number from 1 to 4.")

def choose_target(type, source):
    input_num = get_num_of_target()
    input_type_list = []
    for i in range(input_num):
        while True: 
            input_type = input(f"{type} currency {i+1} (SGD, JPY, MYR, CNY, USD): ").upper()
            if(input_type in type_list): 
                if (input_type == source):
                        print("Target currency should different with Source currency")
                        continue
                input_type_list.append(input_type.upper())
                break
            else:
                print("Invalid currency. Please use SGD, JPY, MYR, CNY or USD.")
    return input_type_list


def convert_currency(input_amount, source, target_list):
    currency_list = {}
    for i in range(len(target_list)):
        exchange_rate = type_list[source][target_list[i]]
        currency = float(input_amount * exchange_rate)
        currency_list[target_list[i]] = round(currency, 2)
    return currency_list

def printResult(input_amount, source, target_list, currency_list):
    print("===RESULT===")
    for i in range(len(target_list)):
        print(f"{input_amount} {source} is equal to {target_list[i]} {currency_list[target_list[i]]}")
            
def should_continue():
    while True:
        print()
        input_answer = input("Continue to the next currency conversion? (Y/N): ").lower()
        if input_answer in should_continue_list:
            return input_answer
        
        print("Invalid answer. Please enter Y or N.")

def printEndingMessage(index):
    print()
    print(f"History: You have conducted {index} currency conversions.")
    print("Thank you!")

def start_convert(index):
    while True:
        print()
        print(f"Currency Conversion {index+1}: ")
        input_amount = validate_input_amount()
        source = choose_source(SOURCE, None)
        target_list = choose_target(TARGET, source)
        currency_list = convert_currency(input_amount, source, target_list)
        printResult(input_amount, source, target_list, currency_list)
        index += 1
        answer = should_continue()
        if answer == NO:
            printEndingMessage(index)
            break
    
def start():
    index = 0
    start_convert(index)

start()