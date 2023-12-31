class UserCreatedEvent:
    def __init__(self, username:str, email:str, role:str):
        self.username = username
        self.email = email
        self.role  = role
    def is_valid(self):
        if not self.username or not self.email:
            return False
        return True