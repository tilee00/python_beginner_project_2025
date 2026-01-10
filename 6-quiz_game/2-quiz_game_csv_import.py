import csv

def process_csv(file_path):
    total_spend = 0
    highest_expense = 0
    item_name = ""

    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            # DictReader treats the first row as headers
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Assuming the CSV has columns 'Item' and 'Price'
                name = row['Item']
                price = float(row['Price'])
                
                total_spend += price
                
                if price > highest_expense:
                    highest_expense = price
                    item_name = name

        # Displaying the results
        print(f"--- Analysis Complete ---")
        print(f"Total Expenses: ${total_spend:.2f}")
        print(f"Most Expensive Item: {item_name} (${highest_expense:.2f})")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except KeyError:
        print("Error: Make sure your CSV has 'Item' and 'Price' headers.")

# Ask the user for the filename
file_input = input("Enter the path to your CSV file: ")
process_csv(file_input)