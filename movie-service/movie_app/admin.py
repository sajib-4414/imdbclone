from django.contrib import admin
from movie_app.models import Movie, StreamPlatform, Review, User

# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(User)