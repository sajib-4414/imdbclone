from fastapi import HTTPException, Request
from model import TokenUser
import json
import requests
from helpers.token_helper import token_creator
# auth_views.py
from fastapi import APIRouter

router = APIRouter()


# Endpoint to generate tokens for login from the client
@router.post("/login/")
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