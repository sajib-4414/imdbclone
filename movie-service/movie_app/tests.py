from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase
from movie_app import serializers
from movie_app import models
import datetime
from movie_app.models import Movie, StreamPlatform

# class StreamPlatformTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='example',
#             password='123$$$$'
#         )
#         self.client.credentials(HTTP_X_USERNAME='example')
#         # self.token = Token.objects.get(user__username=self.user)
#         # self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
#         kwargs = {
#             "name": "Netflix",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         self.stream = models.StreamPlatform.objects.create(**kwargs)
    
#     # this view requires admin credential to do things.
#     def test_streamplatform_create_without_logged_in(self):
#         client_without_auth = APIClient()
#         data = {
#             "name": "Netflix",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         response = client_without_auth.post(reverse('streamplatform-list'), data) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
#     # this view requires admin credential to do things.
#     def test_streamplatform_create_logged_in_regular_user(self):
#         data = {
#             "name": "Netflix",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         response = self.client.post(reverse('streamplatform-list'), data) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
#     def test_streamplatform_list_get(self):
#         response = self.client.get(reverse('streamplatform-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#     def test_streamplatform_list_individual_get(self):
#         response = self.client.get(reverse('streamplatform-detail', args=[self.stream.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#     # this view requires admin credential to update.
#     def test_streamplatform_update(self):
#         data = {
#             "name": "Netflix-updated",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         response = self.client.put(reverse('streamplatform-detail', args=[self.stream.id]), data) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
#     # this view requires admin credential to delete.
#     def test_streamplatform_delete(self):
#         response = self.client.delete(reverse('streamplatform-detail', args=[self.stream.id])) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# class WatchListTestCase(APITestCase):
    
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='example',
#             password='123$$$$'
#         )
#         self.token = Token.objects.get(user__username=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
#         kwargs = {
#             "name": "Netflix",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         self.stream = models.StreamPlatform.objects.create(**kwargs)
#         self.movie = models.Movie.objects.create(platform=self.stream, title="Rocky handsome movie",
#                                                          storyline = "A brave movie", active=True)
        
        
        
    
#     def test_watchlist_create_without_auth(self):
#         client_without_auth = APIClient()
#         data = {
#             "platform":self.stream,
#             "title": "Cinderalla",
#             "Storyline": "Revolves around the queen",
#             "active": True
#         }
#         response = client_without_auth.post(reverse('movie-list'),data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
#     def test_watchlist_create_regular_user(self):
#         data = {
#             "platform":self.stream,
#             "title": "Cinderalla",
#             "Storyline": "Revolves around the queen",
#             "active": True
#         }
#         response = self.client.post(reverse('movie-list'),data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
#     def test_watchlist_listing(self):
#         response = self.client.get(reverse('movie-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#     def test_watchlist_individual_get(self):
#         response = self.client.get(reverse('movie-detail', args=[self.movie.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(models.Movie.objects.count(), 1)
#         self.assertEqual(models.Movie.objects.get().title, 'Rocky handsome movie')
    
#     # this view requires admin credential to update.
#     def test_watchlist_update(self):
#         data = {
#             "title": "new title",
#             "storyline": "new storyline",
#             "active": True
#         }
#         response = self.client.put(reverse('movie-detail', args=[self.movie.id]), data) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
#     # this view requires admin credential to delete.
#     def test_watchlist_delete(self):
#         response = self.client.delete(reverse('movie-detail', args=[self.movie.id])) # viewset creates viewnames like this
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
# class ReviewTestCase(APITestCase):
    
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='example',
#             password='123$$$$'
#         )
#         self.token = Token.objects.get(user__username=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
#         kwargs = {
#             "name": "Netflix",
#             "about": "#1 streaming platform",
#             "website": "https://netflix.com"
#         }
#         self.stream = models.StreamPlatform.objects.create(**kwargs)
#         self.movie = models.Movie.objects.create(platform=self.stream, title="Rocky handsome movie",
#                                                          storyline = "A brave movie", active=True)
#         self.movie2 = models.Movie.objects.create(platform=self.stream, title="Rocky handsome movie",
#                                                          storyline = "A brave movie", active=True)
#         self.review = models.Review.objects.create(movie=self.movie2, review_user=self.user, rating=5,
#                                                      description="Awesome movie", active=True)
        
#     def test_review_create(self):
#         data = {
#             "movie":self.movie,
#             "user":self.user,
#             "rating":5,
#             "description":"Awesome movie",
#             "active":True
#         }
#         response = self.client.post(reverse('review-create', args=[self.movie.id]),data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#         self.assertEqual(models.Review.objects.count(), 2)
#         self.assertEqual(models.Review.objects.first().description, 'Awesome movie')
        
#         # review is not allowed to be created second time, one person one review only
#         response = self.client.post(reverse('review-create', args=[self.movie.id]),data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
#     def test_review_create_un_authorized(self):
#         data = {
#             "movie":self.movie,
#             "user":self.user,
#             "rating":5,
#             "description":"Awesome movie",
#             "active":True
#         }
#         self.client.force_authenticate(user=None) # means not logged in
#         response = self.client.post(reverse('review-create', args=[self.movie.id]),data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
#     def test_review_update(self):
#         data = {
#             "movie":self.movie,
#             "user":self.user,
#             "rating":2,
#             "description":"Awesome movie updated",
#             "active":False
#         }
#         response = self.client.put(reverse('review-detail', args=[self.review.id]),data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_review_list(self):
#         response = self.client.get(reverse('review-list',args=[self.movie.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_review_individual(self):
#         response = self.client.get(reverse('review-detail',args=[self.review.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_review_delete(self):
#         response = self.client.delete(reverse('review-detail',args=[self.review.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
#     def test_review_user(self):
#         response = self.client.get('/api/v1/movies/user-reviews/?username='+self.user.username)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        

# class MovieTestCase(TestCase):
#     # we are testing the batch query performance, and index performance
#     def setUp(self):
#         start_time = datetime.datetime.now()
#         movies = []
#         size = 500
#         platform = StreamPlatform()
#         platform.name = "dummy"
#         platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
#         platform.about = "this is a dummy platform dont worry"
#         platform.save()
        
#         bulk_create = True
#         if bulk_create:
#             for i in range(100000):
#                 movie = Movie()
#                 movie.title = f"title{i}"
#                 movie.storyline = f"storyline{i}"
#                 movie.platform = platform
#                 movies.append(movie)
#             Movie.objects.bulk_create(movies, size)
#         else:
#             for i in range(100000):
#                 movie = Movie()
#                 movie.title = f"title{i}"
#                 movie.storyline = f"storyline{i}"
#                 movie.platform = platform
#                 movie.save()

#         end_time = datetime.datetime.now()
#         print(f"Create method execution time: {end_time - start_time}")

#     def test_lookup(self):
#         start_time = datetime.datetime.now()
#         for i in range(50000, 51000):
#             Movie.objects.get(title=f"title{i}")

#         end_time = datetime.datetime.now()
#         print(f"Get method execution time: {end_time - start_time}")

# class MoviePlatformNameRetrievalTestCase(TestCase):
#     def setUp(self):
#         start_time = datetime.datetime.now()
#         platform = StreamPlatform()
#         platform.name = "dummy"
#         platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
#         platform.about = "this is a dummy platform dont worry"
#         platform.save()
#         Movie.objects.create(title="Movie title1", platform=platform, storyline="Storyline1")

#         end_time = datetime.datetime.now()
#         print(f"Create method execution time: {end_time - start_time}")

#     def test_without_select(self):
#         # print(Movie.objects.all())
#         # print(Movie.objects.get(pk=1))
#         movie = Movie.objects.get(title="Movie title1")
#         movie.platform.name
#         start_time = datetime.datetime.now()
#         for _ in range(100000):
#             movie = Movie.objects.get(title="Movie title1")
#             movie.platform.name

#         end_time = datetime.datetime.now()
#         print(f"Without select execution time: {end_time - start_time}")

#     def test_with_select(self):
#         start_time = datetime.datetime.now()
#         for _ in range(100000):
#             movie = Movie.objects.select_related("platform").get(pk=1)
#             movie.platform.name

#         end_time = datetime.datetime.now()
#         print(f"With select execution time: {end_time - start_time}")
   

        
# class MovieRetrievalFromPlatformTestCase(TestCase):
#     def setUp(self):
#         start_time = datetime.datetime.now()
#         platform = StreamPlatform()
#         platform.name = "dummy"
#         platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
#         platform.about = "this is a dummy platform dont worry"
#         platform.save()
#         Movie.objects.create(title="Movie title1", platform=platform, storyline="Storyline1")

#         end_time = datetime.datetime.now()
#         print(f"Create method execution time: {end_time - start_time}")

#     def test_without_prefetch_related(self):
#         platform = StreamPlatform.objects.get(name="dummy")
#         start_time = datetime.datetime.now()
#         for _ in range(1000000):
#             movies = platform.movies.all()
#             # print(movies)

#         end_time = datetime.datetime.now()
#         print(f"Without prefetch related execution time: {end_time - start_time}")

#     def test_with_prefetch_related(self):
#         platform = StreamPlatform.objects.prefetch_related('movies').get(pk=1)
#         start_time = datetime.datetime.now()
#         for _ in range(1000000):
#             movies = platform.movies.all()

#         end_time = datetime.datetime.now()
#         print(f"With prefetch related execution time: {end_time - start_time}")

# class MovieRetrievalWithDeferTestCase(TestCase):
#     def setUp(self):
#         start_time = datetime.datetime.now()
#         platform = StreamPlatform()
#         platform.name = "dummy"
#         platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
#         platform.about = "this is a dummy platform dont worry"
#         platform.save()
#         Movie.objects.create(title="Movie title1", platform=platform, storyline="Storyline1")

#         end_time = datetime.datetime.now()
#         print(f"Create method execution time: {end_time - start_time}")

#     def test_without_defer(self):
#         start_time = datetime.datetime.now()
#         for _ in range(10000):
#             Movie.objects.get(title="Movie title1")

#         end_time = datetime.datetime.now()
#         print(f"Without defer execution time: {end_time - start_time}")

#     def test_with_defer(self):
#         start_time = datetime.datetime.now()
#         for _ in range(10000):
#             Movie.objects.defer("storyline", "platform").get(title="Movie title1")

#         end_time = datetime.datetime.now()
#         print(f"With defer execution time: {end_time - start_time}")

# class MovieRetrievalWithCountTestCase(TestCase):
#     def setUp(self):
#         start_time = datetime.datetime.now()
#         platform = StreamPlatform()
#         platform.name = "dummy"
#         platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
#         platform.about = "this is a dummy platform dont worry"
#         platform.save()
#         Movie.objects.create(title="Movie title1", platform=platform, storyline="Storyline1")
#         Movie.objects.create(title="Movie title2", platform=platform, storyline="Storyline2")

#         end_time = datetime.datetime.now()
#         print(f"Create method execution time: {end_time - start_time}")

#     def test_without_count(self):
#         start_time = datetime.datetime.now()
#         for _ in range(100000):
#             movies = Movie.objects.all()
#             num_movies = len(movies)

#         end_time = datetime.datetime.now()
#         print(f"Without count execution time: {end_time - start_time}")

#     def test_with_count(self):
#         start_time = datetime.datetime.now()
#         for _ in range(100000):
#             num_movies = Movie.objects.all().count()

#         end_time = datetime.datetime.now()
#         print(f"With count execution time: {end_time - start_time}")
from django.core.cache import cache
class MovieRetrievalWithCountTestCase(TestCase):
    def setUp(self):
        start_time = datetime.datetime.now()
        platform = StreamPlatform()
        platform.name = "dummy"
        platform.website = "https://python.plainenglish.io/django-optimization-guide-make-your-app-run-10x-faster-8c2f6d49ff27"
        platform.about = "this is a dummy platform dont worry"
        platform.save()
        Movie.objects.create(title="Movie title1", platform=platform, storyline="Storyline1")
        Movie.objects.create(title="Movie title2", platform=platform, storyline="Storyline2")

        end_time = datetime.datetime.now()
        print(f"Create method execution time: {end_time - start_time}")

    def test_with_cache(self):
        start_time = datetime.datetime.now()
        movies = Movie.objects.all()
        cache.set('movies', movies,3600)
        for _ in range(100000):
            movies = cache.get('movies')
            # if not movies:
            #     movies = Movie.objects.all()
        end_time = datetime.datetime.now()
        print(f"With cache execution time: {end_time - start_time}")

    def test_without_cache(self):
        start_time = datetime.datetime.now()
        for _ in range(100000):
            movies = Movie.objects.all()
        end_time = datetime.datetime.now()
        print(f"Without cache execution time: {end_time - start_time}")