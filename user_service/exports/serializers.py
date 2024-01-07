from rest_framework import serializers
from exports.models import Export
from user_app.api.serializers import UserSerializer

class ExportSerializer(serializers.ModelSerializer):
    creator = UserSerializer()  
    class Meta:
        model = Export
        fields = '__all__'