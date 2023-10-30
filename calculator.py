import math

class Calculator:
    def __init__(self):
        self.result = None

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            print("Error! Division by zero is not allowed.")
        else:
            self.result = x / y

    def power(self, x, y):
        self.result = x ** y

    def root(self, x, y):
        self.result = x ** (1 / y)

    def square_root(self, x):
        self.result = math.sqrt(x)

    def sin(self, x):
        self.result = math.sin(x)

# Rest of your code remains the same with the addition of sin operation

calc = Calculator()

options = {
    "1": "Add",
    "2": "Subtract",
    "3": "Multiply",
    "4": "Divide",
    "5": "Power",
    "6": "Root",
    "7": "Square Root",
    "8": "Sin",
    "9": "Exit"
}

while True:
    print("\nSelect an operation:")
    for key, value in options.items():
        print(f"{key}: {value}")

    choice = input("Enter your choice: ")

    if choice == "9":
        print("Calculator closed.")
        break

    if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
        if choice == "1":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            calc.add(x, y)

        elif choice == "2":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            calc.subtract(x, y)

        elif choice == "3":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            calc.multiply(x, y)

        elif choice == "4":
            x = float(input("Enter dividend: "))
            y = float(input("Enter divisor: "))
            calc.divide(x, y)

        elif choice == "5":
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            calc.power(x, y)

        elif choice == "6":
            x = float(input("Enter number: "))
            y = float(input("Enter root degree: "))
            calc.root(x, y)

        elif choice == "7":
            x = float(input("Enter number: "))
            calc.square_root(x)

        elif choice == "8":
            x = float(input("Enter the angle (in radians): "))
            calc.sin(x)

        if calc.result is not None:
            print("Result:", calc.result)
    else:
        print("Invalid choice. Please select a valid option.")
