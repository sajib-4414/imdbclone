from rest_framework import serializers
# from movie_app.serializers.movie_serializers import MovieSerializer
from movie_app.models import StreamPlatform
class StreamPlatformSerializer(serializers.ModelSerializer):
# creates link instead of ID in the response
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # movie = MovieSerializer(many=True, read_only=True) # this is the related name field, remember
    #we have related_name watchlist in the model foreign key declaration
    
    # it will show only watchlist names, which is the output of __str__ method. 
    # https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield   
    # watchlist = serializers.StringRelatedField(many=True)
    
    #shows only the primary keys of the watchlist objects
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # shows the link for the objects, for this we had to pass the context in the view method
    # watchlist =  serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'..
    # )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__" #when serializing all fields of a model...
    
    # #Object level validation
    # def validate(self, payloadData):
    #     if payloadData['name'] == payloadData['description']:
    #         raise serializers.ValidationError("Name and Description cannot be same")
    #     return payloadData
    
    # # Field level validation
    # def validate_name(self, payloadValue):
    #     if len(payloadValue)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return payloadValue
    
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length

