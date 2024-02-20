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
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

machine_is_on = True


def process_coins(money):
    """Verified the budget the user insert in the machine and return the total"""
    customer_quarters = int(input("How many quarters?: "))
    customer_dimes = int(input("How many dimes?: "))
    customer_nickles = int(input("How many nickels?: "))
    customer_pennies = int(input("How many pennies?: "))

    quarters = customer_quarters * .25
    dimes = customer_dimes * 0.10
    nickles = customer_nickles * 0.05
    pennies = customer_pennies * 0.01

    total = money + quarters + dimes + nickles + pennies
    return total


def update_resources(ingredient, choice):
    """Update the current value of the resources"""
    for item, amount in choice.items():
        if item in ingredient:
            if ingredient[item] >= amount:
                ingredient[item] -= amount
            else:
                print(f"Sorry, there is not enough {item} to make your drink.")
                return False
    return True


def check_resource(customer_selection):
    """Check if the resource is enough to complete the drink"""
    if customer_selection in MENU:
        return update_resources(resources, MENU[customer_selection])
    else:
        print("Invalid selection.")
        return False


def process_payment(drink_cost):
    total_payment = process_coins(0)
    if total_payment >= drink_cost:
        change = total_payment - drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while machine_is_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_choice == "off":
        machine_is_on = False
        print("Good bye!")
    elif customer_choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: ${profit:.2f}")
    else:
        drink = MENU.get(customer_choice)
        if drink:
            if check_resource(customer_choice):
                if process_payment(drink["cost"]):
                    profit += drink["cost"]
                    make_coffee(customer_choice, drink["ingredients"])
        else:
            print("Invalid selection.")
