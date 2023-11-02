from fastapi import FastAPI, Response, HTTPException, Header
from model import TokenUser
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

# Define a secret key for JWT token signing (keep this secret)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Adjust expiration time as needed

# Secret key used to encode and decode JWT tokens
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Function to validate a JWT token
def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # You can add additional checks here, e.g., checking expiration
        return payload
    except JWTError:
        return None


# Endpoint to generate tokens (similar to your code)
@app.post("/token/create/")
def create_token(user: TokenUser):
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user.username,
        "exp": expires,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}

# Validates a given JWT token        
@app.get("/")
async def validate_jwt_token(authorization: str = Header(None)):
    # auth = False
    # if auth:
    #     raise HTTPException(status_code=401, detail="Unauthorized")
    # return Response(status_code=204) 
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    

    token = authorization.replace("Bearer ", "")
    payload = validate_token(token)
    if payload:
        # Token is valid
        return {"message": "Token is valid", "payload": payload}
    else:
        # Token is invalid
        raise HTTPException(status_code=401, detail="Invalid token")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8003)
