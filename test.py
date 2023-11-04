import grpc
from login_proto import login_grpc_pb2, login_grpc_pb2_grpc


with grpc.insecure_channel('localhost:50051') as channel:
    print('----- Second test -----')
    stub2 = login_grpc_pb2_grpc.UserLoginServiceStub(channel)
    print('----- Delete -----')
    response = stub2.ValidateUser(login_grpc_pb2.UserValidationRequest(username='arefin',password='1234'))
    print(response, end='')