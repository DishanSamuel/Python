import random

def life_lost():
    return life-1


print('welcome to number guessing game \n I am thinking of a number between 0 and 100 guess it ')

random_number = random.randint(0,100)
print(f'test {random_number}')

level = input('easy or hard : ')

if level == 'easy':
    life = 10
if level == 'hard':
    life = 5
    
loop = True

while loop:
    print(f'you have {life} lifes left ')
    
    guess = int(input('make a guess : \n'))
    if guess == random_number:
        print('you won')
        loop = False
        
    if guess < random_number:
        print('low guess try again')
        life = life_lost()
        
    if guess > random_number:
        print('high guess try again')
        life = life_lost()
        
    if life == 0:
        print('you lost please try again ')
        loop = False
    