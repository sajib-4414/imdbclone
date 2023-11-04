from django_grpc_framework.test import RPCTestCase
from login_proto import login_grpc_pb2_grpc, login_grpc_pb2
from django.contrib.auth.models import User

class LoginValidateTest(RPCTestCase):
    def test_login_validate(self):
        #creating a test user
        User.objects.create_user(
            username='tom',
            password='1234',
            email='tom@account.com'
        )
        #now checking the grpc user
        stub = login_grpc_pb2_grpc.UserLoginServiceStub(self.channel)
        response = stub.ValidateUser(login_grpc_pb2.UserValidationRequest(username='tom', password='1234'))
        self.assertEqual(response.username, 'tom')
        self.assertEqual(response.email, 'tom@account.com')
    