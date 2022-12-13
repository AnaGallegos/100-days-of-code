from msilib.schema import Class
from unicodedata import name
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#1

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on == True:
    option = menu.get_items()
    choice = input(f'Wich coffee do you want? {option} ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(money_machine.report())
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    

