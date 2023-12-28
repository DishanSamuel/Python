def filter_function(x):
    return x>3

l = [1, 2, 4, 6, 4, 3]

new_l =list(filter(filter_function, l))

print(new_l)