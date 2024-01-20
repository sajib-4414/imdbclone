# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import login_grpc_pb2 as login__grpc__pb2


class UserLoginServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidateUser = channel.unary_unary(
                '/login_proto.UserLoginService/ValidateUser',
                request_serializer=login__grpc__pb2.UserValidationRequest.SerializeToString,
                response_deserializer=login__grpc__pb2.UserValidationResponse.FromString,
                )


class UserLoginServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ValidateUser(self, request, context):
        """Method to validate user credentials
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserLoginServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ValidateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateUser,
                    request_deserializer=login__grpc__pb2.UserValidationRequest.FromString,
                    response_serializer=login__grpc__pb2.UserValidationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'login_proto.UserLoginService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserLoginService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ValidateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/login_proto.UserLoginService/ValidateUser',
            login__grpc__pb2.UserValidationRequest.SerializeToString,
            login__grpc__pb2.UserValidationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)