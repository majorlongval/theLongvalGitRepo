from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from pudb import set_trace

# create a menu object
my_menu = Menu()
mr_coffee = CoffeeMaker()
mr_burns = MoneyMachine()


while True:
 # print "what would you like"
    choice = input(f"What would you like {my_menu.get_items()}\n\n>> ")

    if choice in my_menu.get_items().split('/'):
        drink = my_menu.find_drink(choice)
        if mr_coffee.is_resource_sufficient(drink):
            print(f"sufficient resources for {drink.name}")
            if mr_burns.make_payment(drink.cost):
                mr_coffee.make_coffee(drink)
        else:
            print("money refunded")

    elif choice == "off":
        print("Shutting down - Goodbye")
        exit()
    elif choice == "report":
        mr_coffee.report()
        mr_burns.report()
        print()
    else:
        print(f"{choice} is not in menu")
