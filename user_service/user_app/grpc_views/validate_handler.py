from user_app.grpc_views.grpc_login_validate_service import LoginService
from login_proto import login_grpc_pb2_grpc


def grpc_handlers(server):
    login_grpc_pb2_grpc.add_UserLoginServiceServicer_to_server(LoginService.as_servicer(), server)