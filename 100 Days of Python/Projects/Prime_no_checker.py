#Write your code below this line 👇
def prime_checker(number):
    prime_no = True
    for i in range (2, number):
        if number % i == 0:
            prime_no = False

            
    if prime_no == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

    
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



#lec no 84
#100 days of coding