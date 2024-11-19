def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a* b

def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b

# Main program
def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    print("Select any one from below:")
    print("1st optoin Add")
    print("2nd option Subtract")
    print("3rd option Multiply")
    print("4th option Divide")
    while True:
        choice = input("Enter any of ur  choice (1/2/3/4): ")
        if choice in operations:
            try:
                num1 = float(input("Enter your first no: "))
                num2 = float(input("Enter your second no: "))
                result = operations[choice](num1, num2)
                print(f"The result for input is: {result}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            if input("Let's do next calculation? (yes/no): ").lower() == 'no':
                break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
    