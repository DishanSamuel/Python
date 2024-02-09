import random
import string

def random_letter(num):
    ran_str = []
    for i in range(0 ,num):
        ran_str += random.choice(string.ascii_letters)              # instead of this we can also use append here 
    return ran_str

def encoding(word):
    if len(word) < 3:
        return word[::-1]
    elif len(word) >= 3:
        word_split = list(word)
        word_split.append(word[0])
        word_split.remove(word[0])
        for i in random_letter(3):
            word_split.append(i)
        for i in random_letter(3):
            word_split.insert(0 ,i)
        finalword = "".join(word_split)
        return finalword;
        
        
    

def decoding(word):
    if len(word) < 3:
        return word[::0]
    elif len(word) >= 3:
        final_word = list(word[3:-3])
        final_word.insert(0, str(final_word[-1]))
        final_word.pop(-1)
        return "".join(final_word)
        
        
        
    
    

if __name__ == '__main__':
    loop = True
    while loop:
        print(''' 
        1 - for encoding
        2 - for decoding
        END - for ending the program
        ''')
        option = (input("Enter the option: \n")).upper()
        if option == "1":
            word = input("Enter the word to encode: \n")
            print("\n\n")
            print(f"The encoded word is {encoding(word)}\n\n\n")
            print("------------------------------------------------------------------------------------------------")
        elif option == "2":
            word = input("Enter the word to decode: \n")
            print("\n\n")           
            print(f" The decoded word is {decoding(word)}\n\n\n")
            print("------------------------------------------------------------------------------------------------")
        elif option == "END":
            loop = False
            print("THANK YOU FOR USING OUT SECURE ENCRYPTION ALGO....LOL")
        else:
            print("Invalid option ")
            loop = False
            break
        
        
