#Classes

class User:
    
    # Attributes
    def __init__(self,id,username):
        self.user_id = id
        self.username = username
        self.followers = 0             #Default Number of followers
        self.following = 0             #Default Number of following
        
    # Methods
    def follow(self,user):
        self.following += 1
        user.followers += 1
    
    
        
user1 = User('001', 'dishan')
user2 = User('002', 'samuel')


user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)