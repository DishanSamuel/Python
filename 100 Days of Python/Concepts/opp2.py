class Person:
    
    def __init__(self,name, occupation):
        self.name = name
        self.occupation = occupation
        
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
        
person1 = Person('dishan', 'software dev')
person2 = Person('someone', 'something')

print(person1.name)
print(person2.name)

person1.info()
person2.info()



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# default constructors 

class test:
    def __init__(self):
        test_value = 0
        print('this is a test object')
        
        
obj1 = test()
    