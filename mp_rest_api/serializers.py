from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = User
        # fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    first_name = serializers.CharField(min_length=8)
    last_name = serializers.CharField(min_length=8)
    
    class Meta:
        model = User
        fields = '__all__'
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'