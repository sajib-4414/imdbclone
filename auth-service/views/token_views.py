# auth_views.py
from fastapi import APIRouter, HTTPException, Header
from fastapi.responses import JSONResponse
from model import TokenUser
from helpers.token_helper import token_creator, validate_token
router = APIRouter()

# Endpoint to generate tokens internally when registration
@router.post("/token/create/")
def create_token(user: TokenUser):
    token = token_creator(user)
    return {"token": token}

# Validates a given JWT token        
@router.get("/")
async def validate_jwt_token(authorization: str = Header(None)):
    if not authorization:
        # raise HTTPException(status_code=401, detail="Authorization header is missing")
        #Letting the destination service handle what happens when authorization is not present
        # Return a response indicating the absence of authentication
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
        return JSONResponse(content=response, headers=headers)

    else:
        # Token is invalid
        raise HTTPException(status_code=401, detail="Invalid token")