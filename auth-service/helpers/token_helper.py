from fastapi import FastAPI, HTTPException, status
from models import TokenUser
from jose import jwt, JWTError
from datetime import datetime, timedelta
from models import Token
app = FastAPI()

# Define a secret key for JWT token signing (keep this secret)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Adjust expiration time as needed
REFRESH_TOKEN_EXPIRE_DAYS = 7
#hi

def token_creator(user: TokenUser):
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user.username,
        "exp": expires,
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    refresh_expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_payload = {"sub": user.username, "exp": refresh_expires}
    refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm=ALGORITHM)

    return Token(access_token=access_token, refresh_token=refresh_token)

# Function to validate a JWT token
def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # You can add additional checks here, e.g., checking expiration
        return payload
    except JWTError:
        return None
    
def refresh_tokens(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user = TokenUser(username=payload.get("sub"), email="")  # Retrieve user details as needed
        return token_creator(user)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )