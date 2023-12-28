def add(fn1, fn2):
    return fn1 + fn2

def subtract(fn1, fn2):
    return fn1 - fn2

def multiply(fn1, fn2):
    return fn1 * fn2

def divide(fn1, fn2):
    return fn1 / fn2

loop1_value = True

while loop1_value:

    n1 = float(input('enter the first number : '))

    loop2_value = True

    while loop2_value:

        print("""        +

        -

        *

        /""")

        opr = input('enter the operator : ')

        n2 = float(input('enter the second number : '))

        if opr == '+':
            ans = add(n1, n2)
            

        if opr == '-':
            ans = subtract(n1, n2)
            
        if opr == '*':
            ans = multiply(n1, n2)
            
        if opr == '/':
            ans = divide(n1, n2)


        print(f"{n1} {opr} {n2} = {ans}")


        loop = input("'yes' to end 'no' to do an other operation : ")

        if loop == 'no':
            loop2_value = True
            n1 = ans
        
        if loop == 'yes':
            loop2_value = False
