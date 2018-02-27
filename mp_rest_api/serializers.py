from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from util.CommonUtil import *

import string

# upper case the first character
class ToUpperCaseFirstChar(serializers.CharField):
    def to_representation(self, value):
        return string.capwords(value)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # field to display
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = ToUpperCaseFirstChar()
    last_name = ToUpperCaseFirstChar() # last_name = serializers.CharField()

    # override original "create" method
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user
    
    # change each item displayed format / style
    # def to_representation(self, user):
        # data = super().to_representation(user)  # get original data
        # formated_data = {
            # "status": "ok",
            # "data" : data,
        # }
        # return formated_data
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'