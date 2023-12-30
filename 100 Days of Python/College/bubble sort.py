global list
def swap(n):
    temp = 0
    temp = list[n]
    list[n] = list[n+1]
    list[n+1] = temp
    
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

for i in range(0,len(list)-1):
    for j in range(0,len(list)-1-i):
        if list[j] > list[j+1]:
            swap(j)
print(list)
