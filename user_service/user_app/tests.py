from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    def test_register(self):
        url = reverse('register')
        data = {
            'username': 'testcase',
            'email': 'testcase@example.com',
            'password': '123456$$$',
            'password2': '123456$$$'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'testcase')
        self.assertEqual(response.data['email'], 'testcase@example.com')

# login and logout has been moved to auth microservice
# class LoginLogoutTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='example',
#             email='example@example.com',
#             password='password123$$$'
#         )
#         self.token = Token.objects.get(user__username='example')
    
#     def test_login(self):
#         data = {
#             'username': 'example',
#             'password': 'password123$$$'
#         }
#         response = self.client.post(reverse('login'),data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_logout(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
#         response = self.client.post(reverse('logout'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
                
        