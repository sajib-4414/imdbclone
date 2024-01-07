from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from django.db import IntegrityError
from user_app.models import ContentCreatorUser, RegularUser

class RegistrationCreatorSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    role = serializers.CharField(read_only=True)  # Read-only role field
    class Meta:
        model = ContentCreatorUser
        fields = ( 'username', 'email', 'password','password2','role')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def validate_email(self, value):
        """
        Check if the email address is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address is already in use.')
        return value
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password and password2 and password != password2:
            raise serializers.ValidationError({'password':'Password and Confirm Password must be the same'})

        return data
    def save(self):
        user = ContentCreatorUser.objects.create(username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user
    
class RegistrationRegularSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    role = serializers.CharField(read_only=True)  # Read-only role field
    class Meta:
        model = RegularUser
        fields = ( 'username', 'email', 'password','password2', 'role')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def validate_email(self, value):
        """
        Check if the email address is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address is already in use.')
        return value
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password and password2 and password != password2:
            raise serializers.ValidationError({'password':'Password and Confirm Password must be the same'})

        return data
    def save(self):
        user = RegularUser.objects.create(username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        print('password set is',self.validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username:
            raise serializers.ValidationError({'username': 'Username is required'})
        if not password:
            raise serializers.ValidationError({'password': 'Password is required'})

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include the fields you want to include