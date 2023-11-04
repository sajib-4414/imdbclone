from fastapi import HTTPException, Request, Body
from model import TokenUser, LoginRequestBody
import json
import requests
from helpers.token_helper import token_creator
# auth_views.py
from fastapi import APIRouter
import grpc
from login_proto import login_grpc_pb2, login_grpc_pb2_grpc
router = APIRouter()


# Endpoint to generate tokens for login from the client
@router.post("/login/")
async def login(request: Request, login_request: LoginRequestBody = Body(...)):
    username = login_request.username
    password = login_request.password
    with grpc.insecure_channel('user-service:50051') as channel:
        stub = login_grpc_pb2_grpc.UserLoginServiceStub(channel)
        response = stub.ValidateUser(login_grpc_pb2.UserValidationRequest(username=username,password=password))
        is_credential_valid = response.valid
        # print(response, end="")
        if is_credential_valid:
            tokenuser = TokenUser(username=username, email=response.email)
            token = token_creator(tokenuser)
            return {"token": token}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Working code to call another service with REST api with docker, just transitioned to GRPC
    # data = {
    #     "username":username,
    #     "password":password
    # }
    # host_url = "http://user-service:8000"
    # user_service_tag = "/user-service/"
    # url_for_login_validate = "api/v1/account/login-validate/"
    # DJANGO_API_URL = host_url + user_service_tag + url_for_login_validate
    # response = ""
    # try:
    #     response = requests.post(DJANGO_API_URL, data=data)
    #     print(response.json())
    #     if response.status_code == 200:
    #         username = response.json()['username']
    #         email = response.json()['email']
    #         tokenuser = TokenUser(username=username, email=email)
    #         token = token_creator(tokenuser)
    #         return {"token": token}
    #     elif response.status_code == 401:
    #         raise HTTPException(status_code=401, detail="Invalid username or password")
    #     else:
    #         print(response)
    #         raise HTTPException(status_code=500, detail="Internal Server Error")
    # except requests.RequestException as e:
    #     print(e)
    #     print("Error connecting to the Django API")
    #     raise HTTPException(status_code=500, detail="Error connecting to the Django API")
    # raise HTTPException(status_code=500, detail="something went wrong")