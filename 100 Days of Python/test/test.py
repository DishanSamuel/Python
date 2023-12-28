print('welcome to the ticket counter')
height = int(input('please enter your height : '))

if height >=  170 :
    print('you are allowed')
    
    age = int(input('enter you age: '))
    
    if  age <= 7:
        print('pay 1$')
    elif age < 18:
        print('pay 2$')
    else:
        print('pay 3$')

else:
    print('you are not allowed')
    
print('hello world')
