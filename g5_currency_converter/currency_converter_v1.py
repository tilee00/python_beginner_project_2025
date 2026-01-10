

# version 1.0

# SGD, MYR, JPY
# 1 SGD = 3.15 MYR
# 1 SGD = 122 JPY
# 1 JPY = 0.026 MYR
# 1 JPY = 0.0082 SGD
# 1 MYR = 0.32 SGD
# 1 MYR = 39 JPY

SGD = "SGD"
JPY = "JPY"
MYR = "MYR"
SOURCE = "Source"
TARGET = "Target"

type_list = {
    SGD: {
        JPY: 121.9577,
        MYR: 3.1535
    },
    JPY: {
        SGD: 0.0082,
        MYR: 0.0259
    },
    MYR : {
        SGD: 0.3171,
        JPY: 38.6734
    }
}

def validate_input_amount():
    while True:
        try:
            input_amount = float(input("Enter the amount: "))
            # IMPROVEMENT: Shoud prevent user enter negative value
            # if input_amount <= 0:
            #     raise ValueError()
            return input_amount
        except:
            print("Please enter a valid amount")

def choose_type(type, source):
    while True:
        input_type = input(f"{type} currency (SGD, JPY, MYR): ").upper()
        if(input_type in type_list): 
            if (source is not None):
                if (input_type == source):
                    print("Target currency should different with Source currency")
                    continue
            return input_type.upper()
        else:
            print("Invalid currency. Please use SGD, JPY, or MYR.")

def convert_currency(input_amount, source, target):
    exchange_rate = type_list[source][target]
    currency = float(input_amount * exchange_rate)
    return round(currency,2)

def start_convert():
    input_amount = validate_input_amount()
    source = choose_type(SOURCE, None)
    target = choose_type(TARGET, source)
    currency = convert_currency(input_amount, source, target)
    print(f"{input_amount} {source} is equal to {currency} {target}")
    

start_convert()