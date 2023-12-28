import random 
import os
from game_data import data

conA=True
conB=True

score_number = 0


def score():
    global score_number
    score_number += 1
    return f"You're right! Current score: {score_number}"


def random_celebA():
    global celeb_dataA
    
    if conA:
        celeb_dataA = random.choice(data)
        return f"Compare A: {celeb_dataA['name']}, {celeb_dataA['description']}, from {celeb_dataA['country']}"
    else:
        return f"Compare A: {celeb_dataA['name']}, {celeb_dataA['description']}, from {celeb_dataA['country']}"

def random_celebB():
    global celeb_dataB
    
    
    if conB:
        celeb_dataB = random.choice(data)
        return f"Compare B: {celeb_dataB['name']}, {celeb_dataB['description']}, from {celeb_dataB['country']}"
    else:
        return f"Compare B: {celeb_dataB['name']}, {celeb_dataB['description']}, from {celeb_dataB['country']}"
        

def verify():

    if celeb_dataA['follower_count'] > celeb_dataB['follower_count']:
        return "A"
    if celeb_dataA['follower_count'] < celeb_dataB['follower_count']:
        return "B"
    
    
loop = True

while loop:
    

    if score_number == 0:
        print(' ')
    else:
        print(f"You're right! Current score: {score_number} ")
        
    print(random_celebA())
    print(celeb_dataA['follower_count'])
    print(random_celebB())
    print(celeb_dataB['follower_count'])
        
    user_input_unmod = input("Who has more followers? Type 'A' or 'B' : ")
    user_input = user_input_unmod.upper()
    
    os.system('cls')
    
    if verify() == user_input:
        score()
    else:
        print(f"Sorry, that's wrong. Final score: {score_number}")
        loop = False
        
    
        
    conA=True
    conB=True
    
    if verify() == 'A':
        conA = False
    if verify() == 'B':
        conB = False
    

#    The Other version of this project (higher_lower(classroom vr).py) is very efficient and practical please refer that to make future code. don't be a shitty coder
    
    
        