# auth_views.py
from fastapi import APIRouter, HTTPException, Header, Body
from fastapi.responses import JSONResponse
from models import TokenUser
from helpers.token_helper import token_creator, validate_token
from models import Token
from helpers.token_helper import refresh_tokens
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
router = APIRouter()

class TokenRefreshRequestBody(BaseModel):
    refresh_token: str
    
# Endpoint to generate tokens internally when registration
@router.post("/token/create/")
def create_token(user: TokenUser):
    token = token_creator(user)
    return {
        "token": token.access_token,
        "refresh_token": token.refresh_token
        }

@router.post("/token/refresh")
def token_refresh(body: TokenRefreshRequestBody):
    tokens = refresh_tokens(body.refresh_token)
    return JSONResponse(content=jsonable_encoder(tokens))

    

# Validates a given JWT token        
@router.get("/")
async def validate_jwt_token(authorization: str = Header(None)):
    print("came here for auth.....")
    if not authorization:
        # raise HTTPException(status_code=401, detail="Authorization header is missing")
        #Letting the destination service handle what happens when authorization is not present
        # Return a response indicating the absence of authentication
        print("1.1......")
        response = {"message": "No authentication header provided"}
        return JSONResponse(content=response, status_code=200)
    token = authorization.replace("Bearer ", "")
    payload = validate_token(token) #contains email and username
    if payload:
        response = {"message": "Authentication Successful"}
        headers = {
            "Content-Type": "application/json",
            "user_email": "test@test.com",
            "X-Username": payload.get("sub"),
        }
        print("1.2......")
        return JSONResponse(content=response, headers=headers)

    else:
        # Token is invalid
        print("1.3......")
        raise HTTPException(status_code=401, detail="Invalid token")