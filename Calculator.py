from art import logo

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

signs = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?"))

    should_continue = True

    while should_continue:
        for operator in signs:
            print(operator)
        symbol = input("Pick an operation from above: ")

        num2 = float(input("What's the second number?"))

        calculation = signs[symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()



