import Menu
switch = "on"
profit = 0
while switch == "on":
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    def process_coins():
        print("Please insert coins.")
        q_dollars = int(input("How many quarters?: ")) * 0.25
        d_dollars = int(input("How many dimes?: ")) * 0.10
        n_dollars = int(input("How many nickles?: ")) * 0.05
        p_dollars = int(input("How many pennies?: ")) * 0.01
        total = q_dollars + d_dollars + n_dollars + p_dollars
        return total

    def report_func():
        print(Menu.resources)

    def is_transaction_successful(money_received, drink_cost):
        if money_received >= drink_cost:
            change = round((money_received - drink_cost))
            print(f"Here is ${change} change")
            global profit
            profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money")
            return False

    def make_coffee(drink_name, order_ingredients):
        for item in order_ingredients:
            Menu.resources[item] -= order_ingredients[item]
        print(f"Here is your {coffee_type}")

    def is_resource_sufficient(order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] >= Menu.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    if coffee_type == "report":
        report_func()
    else:
        drink = Menu.MENU[coffee_type]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_type, drink["ingredients"])

    switch = input("Type 'off' if you want to turn off the machine else type 'on': ").lower()
