from django.contrib import admin
from watchlist_app.models import Movie, StreamPlatform, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(Review)
