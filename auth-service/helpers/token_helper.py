from fastapi import FastAPI
from model import TokenUser
from jose import jwt, JWTError
from datetime import datetime, timedelta
app = FastAPI()

# Define a secret key for JWT token signing (keep this secret)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Adjust expiration time as needed

def token_creator(user: TokenUser):
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user.username,
        "exp": expires,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Function to validate a JWT token
def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # You can add additional checks here, e.g., checking expiration
        return payload
    except JWTError:
        return None