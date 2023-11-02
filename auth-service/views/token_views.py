# auth_views.py
from fastapi import APIRouter, HTTPException, Header
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
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    token = authorization.replace("Bearer ", "")
    payload = validate_token(token)
    if payload:
        # Token is valid
        return {"message": "Token is valid", "payload": payload}
    else:
        # Token is invalid
        raise HTTPException(status_code=401, detail="Invalid token")