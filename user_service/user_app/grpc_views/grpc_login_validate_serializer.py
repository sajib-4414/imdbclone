from django_grpc_framework import proto_serializers
from login_proto import login_grpc_pb2
from rest_framework import serializers
from django.contrib.auth.models import update_last_login  # Import Django's User model
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()

class LoginProtoSerializer(proto_serializers.ProtoSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)  # Added password field as write-only
    class Meta:
        model = User
        proto_class = login_grpc_pb2.UserValidationResponse
        # fields = ['id', 'title', 'content']
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        

        # Authenticate the user based on username and password...
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid username or password')
        
        update_last_login(None, user)

        return user
    def to_representation(self, instance):
        # Customize the serialized representation of the User instance
        return {
            'username': instance.username,
            'email': instance.email,
            'name': instance.username,
            'role': instance.role,
            'valid':True
        }