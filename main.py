import art

# Define basic arithmetic functions
def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Return the quotient of two numbers."""
    return n1 / n2

# Dictionary to map symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """
    A simple calculator that performs basic arithmetic operations (+, -, *, /).
    
    The user can continue to calculate using the result of the previous operation or start a new calculation.
    """
    should_accumulate = True
    
    # Display logo from art file
    print(art.logo)
    
    # Get the first number from the user
    num1 = float(input("What's the first number?\n"))

    while should_accumulate:
        # Display available operations
        for symbol in operations:
            print(symbol)
        
        # Get the operation and the next number
        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("What's the next number?\n"))
        
        # Perform the calculation
        result = operations[operation_symbol](num1, num2)
        
        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {result}")
        
        # Ask the user if they want to continue with the result or start a new calculation
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n").lower()
        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()  # Restart the calculator

# Start the calculator program
calculator()
