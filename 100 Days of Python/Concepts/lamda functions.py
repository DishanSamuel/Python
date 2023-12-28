def double(x):
    return x*2

#using a function inside a function

def funinfun(fx, value):
    return fx(value) + value


double_lambda = lambda x:x*2
add_lambda = lambda x,y,z : x + y + z



print(double(5))
print(double_lambda(5))
print(add_lambda(5,2,10))
print(funinfun(double_lambda, 10))



# both the lambda and the def double(x) function are almost the same it can be used according to the problem while coding