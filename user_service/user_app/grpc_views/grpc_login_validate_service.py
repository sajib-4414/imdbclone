import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from user_app.grpc_views.grpc_login_validate_serializer import LoginProtoSerializer #, PostProtoSerializer

class LoginService(Service):

    def ValidateUser(self, request, context):
        print(request.username)
        serializer = LoginProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        return serializer.message