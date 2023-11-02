from fastapi import FastAPI, Response, HTTPException, Header, Request
import httpx
from model import TokenUser
from jose import jwt, JWTError
from datetime import datetime, timedelta
import json
import requests
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


# Endpoint to generate tokens internally when registration
@app.post("/token/create/")
def create_token(user: TokenUser):
    token = token_creator(user)
    return {"token": token}

# Endpoint to generate tokens for login from the client
@app.post("/login/")
async def login(request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode("utf-8")  # Decode the bytes to a string
    data = json.loads(body_str)  # Deserialize the JSON data
    DJANGO_API_URL = "http://user-service:8000/user-service/api/v1/account/login-validate/"



    response = ""
    try:
        response = requests.post(DJANGO_API_URL, data=data)
        print(response.json())
        username = response.json()['username']
        email = response.json()['email']
        
        if response.status_code == 200:
            tokenuser = TokenUser(username=username, email=email)
            token = token_creator(tokenuser)
            return {"token": token}
        elif response.status_code == 401:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        else:
            print(response)
            raise HTTPException(status_code=500, detail="Internal Server Error")
    except requests.RequestException as e:
        print(e)
        print("Error connecting to the Django API")
        raise HTTPException(status_code=500, detail="Error connecting to the Django API")
    raise HTTPException(status_code=500, detail="something went wrong")

def token_creator(user: TokenUser):
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user.username,
        "exp": expires,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


# Validates a given JWT token        
@app.get("/")
async def validate_jwt_token(authorization: str = Header(None)):
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
