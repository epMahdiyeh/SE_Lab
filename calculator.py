#functions

options = {
    "1": "Add",
    "2": "Subtract",
    "3": "Multiply",
    "4": "Divide",
    "5": "Power",
    "6": "Root",
    "7": "Square Root",
    "8": "Exit"
}

while True:
    print("\nSelect an operation:")
    for key, value in options.items():
        print(f"{key}: {value}")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Calculator closed.")
        break