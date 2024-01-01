global list
list=[]
def swap(n):
    temp = list[n]
    list[n] = list[n+1]
    list[n+1] = temp
def input_numbers():
    numbers = int
    input_code = 0
    loop = True
    while loop:
        input_code = input('Enter the numbers to sort : ')
        if input_code == 'end':
            loop = False
            print('okay')
            break
        elif input_code != 'end':
            try:
                numbers = int(input_code)
            except ValueError:
                print("Invalid input")
                break
            list.append(numbers)
def main():
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1-i):
            if list[j] > list[j+1]:
                swap(j)

#only for this module
if __name__ == "__main__":
    input_numbers()
    print(list)
    main()
    print(list)

#for binary search module
input_numbers()
main()
