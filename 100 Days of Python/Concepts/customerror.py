number = int(input("Enter the number between 5 and 10 : "))

if (number < 5 or number > 10):
    raise Exception("Number must be between 5 and 10")             #there are many types of error/exceptions we can use (refer the internet)