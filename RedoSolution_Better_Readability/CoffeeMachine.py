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
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

is_on = True


def process_coin():
    """Return the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.10
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted and False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        break # Add a break statement to exit the loop
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

