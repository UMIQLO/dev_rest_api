from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from util.CommonUtil import *

import string

class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return string.capwords(value)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = ToUpperCaseCharField()
    last_name = ToUpperCaseCharField() # last_name = serializers.CharField()

    # override original create method
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user
    
    # change each item displayed format / style
    def to_representation(self, user):
        data = super().to_representation(user)  # the original data

        return {
            '$jason': {
                'head': {
                    
                },
                'body': data,
            }
        }
    
    class Meta:
        model = User
        # field to display
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'