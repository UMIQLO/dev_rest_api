from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'