# CODE WITH HARRY LEC 60

class MyClass():
    
    def __init__(self, _value):
        self._value = _value
        
    def show(self):
        print(f'The Value is {self._value}')
        
    
    @property                                                                  #*--> this is a getter decorator
    def ten_value(self):
        return self._value * 10
    
    
    @ten_value.setter                                                           #*--> this is a setter decorator    
    def ten_value(self, new_value):
        self._value = new_value/10
        
        
        
obj = MyClass(10)
obj.show()
obj.ten_value = 69                                                              #*--> here we are using the setter decorator
obj.show()
print(obj.ten_value)                                                             #*--> here we are using the getter decorator
obj.show()
