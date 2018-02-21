from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from util.CommonUtil import *

class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return ''

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = ToUpperCaseCharField()
    # password = serializers.CharField(min_length=8)
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        # field to display
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'