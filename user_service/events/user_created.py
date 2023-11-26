class UserCreatedEvent:
    def __init__(self, username:str, email:str):
        self.username = username
        self.email = email
    def is_valid(self):
        if not self.username or not self.email:
            return False
        return True