# CODE WITH HARRY (PYTHON) LEC - 57

class person:
    name = 'dishan'
    occupation = 'software Engineer'
    
    # THIS IS A METHOD
    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = person()
b = person()
b.name = 'someone'
b.occupation = 'something'


print(a.occupation) 
print(b.occupation)

a.info()
b.info()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# A AND B BECOMES TWO DIFFERENT IDENTITIES
# THAT IS WHY 'CLASS' ARE KNOWN AS A BLUEPRINT
