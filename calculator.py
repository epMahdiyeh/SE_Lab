import math

class Calculator:
    #TO DO
    pass


calc = Calculator()

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

    if choice in ("1", "2", "3", "4", "5", "6", "7"):
        if choice == "1":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            calc.add(x, y)

        elif choice == "2":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            calc.subtract(x, y)