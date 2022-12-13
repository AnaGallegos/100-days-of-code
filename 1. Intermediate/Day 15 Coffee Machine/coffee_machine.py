MENU = {
    "expresso": {
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
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

profit = 0
   
def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True 

def input_money():
    money = 0
    money =  int(input('How many quarters? ')) * 0.25
    money += int(input('How many dimes? ')) * 0.1
    money += int(input('How many nickles? ')) * 0.05
    money += int(input('How many pennies? ')) * 0.01
    print(f'You have inserted {money}$')
    return money
    
def is_money_sufficient(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        global profit
        profit += cost
        if change > 0:
            print(f'Thank you, your change is {change}$ ')
            return True
    else:
        print('Not enough money, returning, money refunded')
        return False

def make_coffee(order_ingredient, drink_name):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'Here\'s your {drink_name}, enjoy! ☕️')

is_on = True

while is_on == True:
    choice = input('Wich coffee do you want (expresso/latte/capucchino) ☕ ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f'money": {profit}')
    elif choice in MENU:
       drink = MENU[choice]
       if is_resource_sufficient(drink['ingredients']):
            payment = input_money()
            if is_money_sufficient(payment, drink['cost']):
                make_coffee(drink['ingredients'], choice)

    else:
        print('I dont understand! Please try again')


 


