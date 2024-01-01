import bubble_sort
print(bubble_sort.list)

found = False
key = int(input('Enter the key you want to search for: '))

low = 0
high = len(bubble_sort.list) - 1

for i in range(0, high):
    mid = int((high + low)/2)
    if bubble_sort.list[mid] == key:
        found = True
        break
    elif key > bubble_sort.list[mid]:
        low = mid + 1
    else:
        high = mid - 1

if found == True:
    print('key found')
    print(f"the key position is {mid}")
elif found == False:
    print('key not there in the given list')



