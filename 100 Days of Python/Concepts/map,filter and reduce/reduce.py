from functools import reduce

def my_sum(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

sum = (reduce(my_sum, numbers))

print(sum)