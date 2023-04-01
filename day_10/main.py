from art import logo
from operations import operations

print(logo)


def calculator():    
    num1 = float(input("Type the first number: "))
    should_continue = True

    while should_continue:
        num2 = float(input("What is the second number: "))
        
        for symbol in operations:
            print(symbol)

        operation = input("select the operation: ")
        calculation_function = operations[operation]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with {answer}: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()