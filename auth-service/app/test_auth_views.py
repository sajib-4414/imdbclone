from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from .main import app
from unittest.mock import patch
import grpc
from login_proto import login_grpc_pb2, login_grpc_pb2_grpc

# Not working yet.
client = TestClient(app)

def test_successful_login_with_mock():
    # Define a valid login request
    

    with patch("grpc.insecure_channel") as mock_insecure_channel:
        # Create a mock gRPC response
        mock_response = login_grpc_pb2.UserValidationResponse()
        # mock_response.valid = True
        # mock_response.email = "user@example.com"
        # mock_response.username = "user"

        # Configure the mock to return the predefined response
        mock_stub = login_grpc_pb2_grpc.UserLoginServiceStub(mock_insecure_channel())
        mock_stub.ValidateUser.return_value = mock_response

        # Make a POST request to the /login/ endpoint
        login_request = {"username": "user", "password": "valid_password"}
        response = client.post("/login/", json=login_request)

        # Assert the response status code (200 OK for a successful login)
        assert response.status_code == 200

        # Assert the response body contains the expected data (e.g., a token)
        assert "token" in response.json()

# def test_invalid_login_with_mock():
#     # Define an invalid login request
#     login_request = {"username": "invalid_username", "password": "invalid_password"}

#     with patch("localhost") as mock_insecure_channel:
#         # Define a mock gRPC response
#         mock_response = login_grpc_pb2.UserValidationResponse(valid=False)

#         # Configure the mock to return the predefined response
#         mock_stub = mock_insecure_channel.return_value
#         mock_stub.ValidateUser.return_value = mock_response

#         # Make a POST request to the /login/ endpoint
#         response = client.post("/login/", json=login_request)

#         # Assert the response status code (401 Unauthorized for an invalid login)
#         assert response.status_code == 401

#         # Assert the response body contains the expected error message
#         assert response.json() == {"detail": "Invalid username or password"}
