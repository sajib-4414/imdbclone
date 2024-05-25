from rest_framework import serializers
from movie_app.models import StreamPlatform, Movie
from movie_app.serializers.streaming_platform_serializers import StreamPlatformSerializer
class MovieSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # a custom populated serializer method field which does not exist on database
    # len_name = serializers.SerializerMethodField()
    platform_id = serializers.PrimaryKeyRelatedField(source='platform', queryset=StreamPlatform.objects.all(), write_only=True)
    platform = StreamPlatformSerializer(read_only=True)
    # platform = serializers.CharField(source='platform.name')
    class Meta:
        model = Movie
        # fields = "__all__" when serializing all fields of a model
        # fields = ('id', 'name', 'description') # if we're serializing some fields only
        exclude = ['active'] # serialize all but active
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

