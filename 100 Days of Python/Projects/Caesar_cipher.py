#REFER LEC 86 (100 DAYS OF PYTHON)
#you can shorten the code by combining the repetitive code with encrypt and decrypt functions and combining them into a single function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True





#if shift number is greater than given alphabet length


def encrypt(plain_text, shift_amount):
    encrypt_text = ''
    for letters in plain_text:
        position =int(alphabet.index(letters))
        new_position = position + shift_amount
        
        if new_position > 25:
            new_position -= 26
            
            
        encrypt_text += alphabet[new_position]
    print(f'The encoded text is {encrypt_text}')    
        
    
def decrypt(plain_text, shift_amount):
    decrypt_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        
        if new_position <0:
            new_position += 25
        decrypt_text += alphabet[new_position]
        
    print(f'The decoded text is {decrypt_text}')     
    
    
while repeat == True:    
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    while shift >24:
        shift -= 24

            
    if direction == 'encode':
        encrypt(plain_text = text,shift_amount= shift)
        
    elif direction == 'decode':
        decrypt(plain_text = text,shift_amount= shift)
        
    else:
        print('The given option is not supported')
        
        
    options = input('Type "yes" if you want to go again . Otherwise Type "no" to end : \n')

    if options == 'no':
        print('GOODBYE')
        repeat = False