# main.py

from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations Tester")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
    # Perform the operation
    result = perform_operation(num1, num2, operation)
    
    # Display the result
    if isinstance(result, str) and result.startswith("Error"):
        print(f"Operation failed: {result}")
    else:
        print(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()