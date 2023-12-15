# MathUtility/uas_[nim].py

from MathUtility.Library.my_library import MathOperations
from gold import calculate_golden_ratio

def main():
    while True:
        print("\nMathUtility Menu:")
        print("1. Basic Math Operations")
        print("2. Calculate Golden Ratio")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            perform_math_operations()
        elif choice == "2":
            calculate_and_display_golden_ratio()
        elif choice == "3":
            print("Exiting MathUtility.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def perform_math_operations():
    math_util = MathOperations()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nMath Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the operation (1-4): ")

    if operation == "1":
        result = math_util.addition(num1, num2)
        print(f"Result: {result}")
    elif operation == "2":
        result = math_util.subtraction(num1, num2)
        print(f"Result: {result}")
    elif operation == "3":
        result = math_util.multiplication(num1, num2)
        print(f"Result: {result}")
    elif operation == "4":
        result = math_util.division(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation. Please enter a valid option.")

def calculate_and_display_golden_ratio():
    result = calculate_golden_ratio()
    print(f"The Golden Ratio is: {result}")

if __name__ == "__main__":
    main()
