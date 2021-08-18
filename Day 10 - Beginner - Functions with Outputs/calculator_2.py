# calculator


# add
def add(n1, n2):
    return n1 + n2

# subtract
def sub(n1, n2):
    return n1 - n2

# multiply
def mul(n1, n2):
    return n1 * n2

# divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    num1 = float(input("Enter the first number? "))
    for key in operations:
        print(key)
    again = "y"
    while again == "y":
        symbol = input("Enter which operation you wanna do? ")
        cal_func = operations[symbol]
        num2 = float(input("Enter the next number? "))
        answer = cal_func(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if again == "y":
            num1 = answer
        else:
            again = "n"
            calculator()
calculator()
