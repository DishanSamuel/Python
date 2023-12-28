def cube(x):
    return x**3

l = [1, 2, 4, 6, 4, 3]

# noob way to cube all the elements in the list

new_list = []
for item in l:
    new_list.append(cube(item))
    
print(new_list)

# pro way

new_list2 =list(map(cube, l))                              # map function always returns a object 
print(new_list2)