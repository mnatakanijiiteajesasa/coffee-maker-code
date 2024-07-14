MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient (order_of_ingredients):
    """"Returns whether the ingredients left are enough to make another drink"""
    for item in order_of_ingredients:
        if order_of_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """" Returns the total value of inserted coins """
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    """Return True if money is enough or false if it is not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!")
        return False


def make_coffee(drink_name,order_of_ingredients):
    """Deduct ingredients from the resources"""
    for item in order_of_ingredients:
        resources[item] -= order_of_ingredients[item]
        print(f"Here is your {drink_name}.Enjoy!")


profit = 0
is_on = True
while is_on:
    customer_choice = input("What would you like?(latte/espresso/cappuccino)\n")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_payment_successful(payment,drink['cost'])
            make_coffee(customer_choice,drink["ingredients"])
