def add(a, b):
    """This function adds two numbers."""
    return a + b

def subtract(a, b):
    """This function subtracts two numbers."""
    return a - b

def main():
    """Main function to demonstrate the add and subtract functions."""
    print("Starting the application.")

    # Demonstrate the add function
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result_add}")

    # Demonstrate the subtract function
    result_subtract = subtract(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is: {result_subtract}")

    print("Application finished.")

if __name__ == "__main__":
    main()