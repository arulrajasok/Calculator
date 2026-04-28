import re

# defining functions first is good practice since python reads line by line

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
def power(a, b):
    return a**b

# Professional approach - short, easier and easy to extend and add more functions
operations = { "+": add, "-": subtract, "*": multiply,"/": divide,"^":power}

def calculator():
    """ Calculator that performs basic arithmetic operations taking numbers with operators while handling input errors and disordered spaces """
    # Compiling the regex once for efficiency
    pattern = r'(-?\d+\.?\d*)\s*([+\-*/^])\s*(-?\d+\.?\d*)'
    regex = re.compile(pattern)
    
    while True:  # we don't need to rerun the code to perform each new operations
        user_input = input("Type the operation here (Eg : '4 + 3' or '5 - 7'): ").strip()
        if user_input.lower() == 'quit':  #lower function solves unnecessary case sensitivity error
            print("Goodbye!")
            break
        match = regex.fullmatch(user_input)
        if not match:
            print("Invalid format. Use: number operator number (e.g., -2.5 * 3)")
            continue
        
        num1 = float(match.group(1))
        operator = match.group(2)
        num2 = float(match.group(3))
            
        func = operations.get(operator)
        if func is None:    # handles unknown function
                print("Unknown Operator")
        else:
            try:
                result = func(num1, num2)
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
            except Exception as e:
                print(f"Invalid input: {e}")
    
#Name guard
if __name__ == "__main__":     # this makes the script importable
    calculator()