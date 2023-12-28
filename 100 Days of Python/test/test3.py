rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


number_human = int(input('what do you choose ? type 0 for rock , 1 for paper , 2 for scissors\n'))

number_bot = random.randint(0,2)


game_image = [rock, paper , scissors]

if number_human < 0 or number_human > 2:
  print('you have typed an invalid number so you lose')

else:


  image_human = game_image[number_human]
  print(image_human)
  
  
  
  
  print('the computer choices:')
  
  
  image_bot = game_image[number_bot]
  print(image_bot)
  
  
  if number_bot == 2 and number_human == 0:
    print('you win')
  
  elif number_human == 2 and number_bot == 0:
    print('you lose')
  
  elif number_human == 1 and number_bot == 0:
    print('you win')
  
  elif number_human == 2 and number_bot == 1:
    print('you win')
  
  elif number_bot > number_human:
    print('you lose')
  
  elif number_bot == number_human:
    print('it is a draw')

  else:
    print('error')
  
