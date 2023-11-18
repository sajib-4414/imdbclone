from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30) # e.g. netflix, amazon, etc
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="movie") # Many to One
    # here streamplatform has many watchlists, so to access the watchlists from a single stream platform
    # we can do this, netflix_watchlist = netflix.watchlist.all()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    number_rating = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True) #if a rview is spam, we inactive it
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True) # writes date when an object is created
    update = models.DateTimeField(auto_now=True) # writes date when an object is created, updated
    
    def __str__(self) -> str:
        return str(self.rating) + ' | ' + self.movie.title + ' | ' + str(self.review_user)