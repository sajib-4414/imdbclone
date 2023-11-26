from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import httpx
import json
from user_app.helpers.serializer_error_parser import parseError
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
            #check if that user already exists or not.
            
            token_data = {
                "username": validated_data['username'],
                "email": validated_data['email'],
                # Add any other necessary data for token creation
            }
            response = httpx.post("http://auth-service:8003/token/create/", json=token_data)
            if response.status_code == 200:
                token = response.json().get("token")
                data['token'] = token
                data['refresh_token'] = response.json().get("refresh_token")
            else:
                # Handle token creation error
                data['token'] = 'Token creation failed'
                raise HttpResponseBadRequest("Token creation failed")

            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            return Response(data, status.HTTP_201_CREATED)
                       
        else:
            return Response(parseError(serializer.errors), status.HTTP_400_BAD_REQUEST)
            
        

@api_view(['POST'])
def login_validate_view(request):

    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        print("request data is")
        print(request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print("validated data is ")
            print(validated_data)
            user = authenticate(request, username=validated_data['username'], password=validated_data['password'])
            if user is not None:
            # The username and password are correct
                login(request, user)  # Log the user in
                return JsonResponse({
                    'username': user.get_username(),
                    'email': user.email
                })
            else:
                # The username and password are not correct
                return JsonResponse({'message': 'Invalid username or password'}, status=401)
        return JsonResponse({'message': 'wrong data'}, status=401)

@api_view(['GET'])
def call_kafka(request):
    if request.method == 'GET':
        from kafka import KafkaProducer
        import pickle
        ORDER_KAFKA_TOPIC = "order_details"
        try:
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            v = {
                'msg': {
                    'hello': 'world',
                },
            }
            serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
            producer.send('Ptopic', serialized_data)
           
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
        return JsonResponse({'message': 'wrong data'}, status=200)