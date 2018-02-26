from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    ### custom json output format (retrieve & list)
    # def retrieve(self, request, *args, **kwargs):
        # return Response({'something': 'my custom JSON retrieve'})
    # def list(self, request, *args, **kwargs):
        # return Response({'something': 'list'})
    
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer