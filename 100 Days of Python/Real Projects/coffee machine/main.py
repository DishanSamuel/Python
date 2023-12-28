# LEC 142
# 100 DAYS OF PYTHON(UDEMY)


from data import MENU



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




    
    
        
loop = True
profit = 0


while loop:
    
    
    
    user_input = input('What would you like? (espresso/latte/cappuccino): ')
    
    if user_input != 'report':
        profit += MENU[user_input]['cost']
    
    resource = {
        'water':300,
        'milk':200,
        'coffee':100,
        'money':profit,
    }
    
    if user_input != 'report':
        for items in MENU[user_input]['ingredients']:
            
            resource[items] -= MENU[user_input]['ingredients'][items]
        
        

    if user_input == 'report':
        for items in resource:
            print(f'{items}:{resource[items]}') 
            
    else:
    
    
    
        quarters = float(input('How many quarters? : '))
        dimes = float(input('How many dimes ? : '))
        nickles = float(input('How many nickles ? : '))
        pennies = float(input('How many pennies ? : '))
        
        total = 0

        total += quarters * 0.25
        total += dimes * 0.10
        total += nickles * 0.05
        total += pennies * 0.01
        
        



        if MENU[user_input]['cost'] <= total:
            balance = float(total -  MENU[user_input]['cost'])
            print(f'Here is ${balance} in change.\nHere is your espresso ☕️. Enjoy!')
        else:
            print("Sorry that's not enough money. Money refunded.")
        
    
    
# you dumb fellow can't even finish this simple project         