from pydantic import BaseModel

# Define a Pydantic model for user data (customize as needed)
class TokenUser(BaseModel):
    username: str
    email: str