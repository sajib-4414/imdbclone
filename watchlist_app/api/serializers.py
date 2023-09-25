from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',) # must be a tuple. we are excluding, as we are using this to create the
        #review also, and we dont want user to input a movie/watchlist id, it should be taaken from the
        #url, and we will set it programmatically, so by excluding this will not enforce watchlist id
        #tobe present in the payload.
      

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # a custom populated serializer method field which does not exist on database
    # len_name = serializers.SerializerMethodField()
    
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        # fields = "__all__" when serializing all fields of a model
        # fields = ('id', 'name', 'description') # if we're serializing some fields only
        exclude = ['active'] # serialize all but active

class StreamPlatformSerializer(serializers.ModelSerializer):
# creates link instead of ID in the response
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) # this is the related name field, remember
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
    #     view_name='movie-detail'
    # )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__" #when serializing all fields of a model
    
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
    
# # a custom validator method, which will be attached with validators property in the serializer
# def name_length(name):
#     if len(name)<2:
#             raise serializers.ValidationError("Name is too short")
#     else:
#         return name

# # these read only, write only are called core arguments of the serializer fileds
# # https://www.django-rest-framework.org/api-guide/fields/#core-arguments
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data): #instance carries old values of the object, validated_data => new values
#         instance.name = validated_data.get('name', instance.name) #updating previous instance's name
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # # Field level validation
#     # def validate_name(self, payloadValue):
#     #     if len(payloadValue)<2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return payloadValue
    
#     #Object level validation
#     def validate(self, payloadData):
#         if payloadData['name'] == payloadData['description']:
#             raise serializers.ValidationError("Name and Description cannot be same")
#         return payloadData

