def swap():
    print(list) 
global list
list = []
numbers = int
input_code = 0
loop = True
while loop:
    input_code = input('Enter the numbers to sort : ')
    if input_code == 'end':
        loop = False
        break
    elif input_code != 'end':
        try:
            numbers = int(input_code)
        except ValueError:
            print("Invalid input")
            break
        list.append(numbers)
print(list)