from inventory import MENU, resources, COINS

profit = 0.0  # Initialize profit


def print_drink_costs(MENU):
    """Prints the cost of each drink in the menu dictionary"""
    for drinks, details in MENU.items():
        print(f"{drinks.capitalize()}: ${details['cost']}")
    return


def get_user_choice():
    """Prompts the user for their choice of drink and check if it matches the menu"""
    print("\n\nWelcome to the Coffee Machine")
    print_drink_costs(MENU)
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice in MENU:
        print(f"You have selected: {user_choice}")
        return user_choice
    elif user_choice == "report":
        print_report(resources, profit)
        return None
    elif user_choice == "off":
        print("Turning off the coffee machine.")
        exit()
    else:
        print("Invalid choice. Please select from Espresso, Latte, or Cappuccino")
        return None


def has_enough_resources(MENU, resources, user_choice):
    """Check if the resources has enough ingredients to make the order"""
    drink_ingredients = MENU[user_choice]["ingredients"]
    for ingredient, amount_required in drink_ingredients.items():
        if amount_required > resources.get(ingredient, 0):
            print(f"Sorry, not enough {ingredient} to make {user_choice}")
            return False  # Not enough resources, exit early
    return True  # Enough resources for the drinks

# put the or 0, so enter will be treated as zero
def process_coins():
    user_quarter = int(input("How many quarters?: ")or 0) * COINS["quarter"]
    user_dimes = int(input("How many dimes?: ")or 0) * COINS["dimes"]
    user_nickles = int(input("How many nickles?: ")or 0) * COINS["nickles"]
    user_pennies = int(input("How many pennies?: ")or 0) * COINS["pennies"]
    total_inserted = user_quarter + user_dimes + user_nickles + user_pennies
    print(f"You have inserted ${total_inserted}")
    return total_inserted


def check_transaction(cost, money_received):
    """Check if the user has inserted enough money to purchase the drink"""
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name}. Enjoy!")


def print_report(resources, profit):
    """Prints the report of remaining resources and total profit"""
    print("\nResource Report:")
    for resource, amount in resources.items():
        unit = "ml" if resource in ["water", "milk"] else "g"
        print(f"{resource.capitalize()}: {amount}{unit}")
    print(f"Money: ${profit}")


# Main program flow
def main():
    while True:
        user_choice = None
        while user_choice is None:
            user_choice = get_user_choice()
            if user_choice is None:
                continue

        if has_enough_resources(MENU, resources, user_choice):
            payment = process_coins()
            if check_transaction(MENU[user_choice]["cost"], payment):
                make_coffee(user_choice, MENU[user_choice]["ingredients"])


if __name__ == "__main__":
    main()
