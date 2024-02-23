from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_machine_on = True

while is_machine_on:
    drink_options = menu.get_items()
    costumer_choice = input(f"What would you want to drink? {drink_options}: ")

    if costumer_choice == "off":
        print("Good Bye!")
        is_machine_on = False
    elif costumer_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(costumer_choice)
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
