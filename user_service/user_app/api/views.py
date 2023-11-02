from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest
import httpx
# from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import RefreshToken
# from user_app.models import * #sometime the signal file doesn't fire, in that case load that file

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    
    
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            token_data = {
                "username": validated_data['username'],
                "email": validated_data['email'],
                # Add any other necessary data for token creation
            }
            response = httpx.post("http://auth-service:8003/token/create/", json=token_data)
            if response.status_code == 200:
                token = response.json().get("token")
                data['token'] = token
            else:
                # Handle token creation error
                data['token'] = 'Token creation failed'
                raise HttpResponseBadRequest("Token creation failed")

            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email

            
            
            
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            # refresh = RefreshToken.for_user(account)
            # data['token'] =  {
            # 'refresh': str(refresh),
            # 'access': str(refresh.access_token),
            # }
            
            
        else:
            data = serializer.errors
            
        return Response(data, status.HTTP_201_CREATED)