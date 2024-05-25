from rest_framework import serializers
from movie_app.models import Movie, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('movie',) # must be a tuple. we are excluding, as we are using this to create the
        #review also, and we dont want user to input a movie/watchlist id, it should be taaken from the
        #url, and we will set it programmatically, so by excluding this will not enforce watchlist id
        #tobe present in the payload.
      