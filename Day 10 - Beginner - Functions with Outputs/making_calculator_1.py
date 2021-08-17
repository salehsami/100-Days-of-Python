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
num1 = int(input("Enter the first number? "))
num2 = int(input("Enter the second number? "))
for key in operations:
    print(key)
symbol = input("Enter which operation you wanna do? ")
cal_func = operations[symbol]
answer = cal_func(num1, num2)
print(f"{num1} {symbol} {num2} = {answer}")
