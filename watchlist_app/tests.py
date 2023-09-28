from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='example',
            password='123$$$$'
        )
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        kwargs = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        self.stream = models.StreamPlatform.objects.create(**kwargs)
    
    # this view requires admin credential to do things.
    def test_streamplatform_create_without_logged_in(self):
        client_without_auth = APIClient()
        data = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        response = client_without_auth.post(reverse('streamplatform-list'), data) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    # this view requires admin credential to do things.
    def test_streamplatform_create_logged_in_regular_user(self):
        data = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_list_get(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_list_individual_get(self):
        response = self.client.get(reverse('streamplatform-detail', args=[self.stream.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # this view requires admin credential to update.
    def test_streamplatform_update(self):
        data = {
            "name": "Netflix-updated",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.put(reverse('streamplatform-detail', args=[self.stream.id]), data) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    # this view requires admin credential to delete.
    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('streamplatform-detail', args=[self.stream.id])) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='example',
            password='123$$$$'
        )
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        kwargs = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        self.stream = models.StreamPlatform.objects.create(**kwargs)
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Rocky handsome movie",
                                                         storyline = "A brave movie", active=True)
        
        
        
    
    def test_watchlist_create_without_auth(self):
        client_without_auth = APIClient()
        data = {
            "platform":self.stream,
            "title": "Cinderalla",
            "Storyline": "Revolves around the queen",
            "active": True
        }
        response = client_without_auth.post(reverse('movie-list'),data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_watchlist_create_regular_user(self):
        data = {
            "platform":self.stream,
            "title": "Cinderalla",
            "Storyline": "Revolves around the queen",
            "active": True
        }
        response = self.client.post(reverse('movie-list'),data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_listing(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_individual_get(self):
        response = self.client.get(reverse('movie-detail', args=[self.watchlist.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Rocky handsome movie')
    
    # this view requires admin credential to update.
    def test_watchlist_update(self):
        data = {
            "title": "new title",
            "storyline": "new storyline",
            "active": True
        }
        response = self.client.put(reverse('movie-detail', args=[self.watchlist.id]), data) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    # this view requires admin credential to delete.
    def test_watchlist_delete(self):
        response = self.client.delete(reverse('movie-detail', args=[self.watchlist.id])) # viewset creates viewnames like this
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='example',
            password='123$$$$'
        )
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        kwargs = {
            "name": "Netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        self.stream = models.StreamPlatform.objects.create(**kwargs)
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Rocky handsome movie",
                                                         storyline = "A brave movie", active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Rocky handsome movie",
                                                         storyline = "A brave movie", active=True)
        self.review = models.Review.objects.create(watchlist=self.watchlist2, review_user=self.user, rating=5,
                                                     description="Awesome movie", active=True)
        
    def test_review_create(self):
        data = {
            "watchlist":self.watchlist,
            "user":self.user,
            "rating":5,
            "description":"Awesome movie",
            "active":True
        }
        response = self.client.post(reverse('review-create', args=[self.watchlist.id]),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(models.Review.objects.count(), 2)
        self.assertEqual(models.Review.objects.first().description, 'Awesome movie')
        
        # review is not allowed to be created second time, one person one review only
        response = self.client.post(reverse('review-create', args=[self.watchlist.id]),data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_review_create_un_authorized(self):
        data = {
            "watchlist":self.watchlist,
            "user":self.user,
            "rating":5,
            "description":"Awesome movie",
            "active":True
        }
        self.client.force_authenticate(user=None) # means not logged in
        response = self.client.post(reverse('review-create', args=[self.watchlist.id]),data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_review_update(self):
        data = {
            "watchlist":self.watchlist,
            "user":self.user,
            "rating":2,
            "description":"Awesome movie updated",
            "active":False
        }
        response = self.client.put(reverse('review-detail', args=[self.review.id]),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_list(self):
        response = self.client.get(reverse('review-list',args=[self.watchlist.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_individual(self):
        response = self.client.get(reverse('review-detail',args=[self.review.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail',args=[self.review.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_review_user(self):
        response = self.client.get('/api/v1/watch/user-reviews/?username='+self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        