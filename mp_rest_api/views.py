from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from .serializers import *
from util.CommonUtil import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).list(request, *args, **kwargs)
        return Response(json_encode(response_data.data, True))
    # create function in serializers
    # def create(self, request, *args, **kwargs):
        # response_data = super(UserViewSet, self).create(request, *args, **kwargs)
        # return Response(json_encode(response_data.data, True))
    def retrieve(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def update(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).update(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def destroy(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).destroy(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    
    def list(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).list(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def create(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).create(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def retrieve(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).retrieve(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def update(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).update(request, *args, **kwargs)
        return Response(json_encode(response_data.data))
    def destroy(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).destroy(request, *args, **kwargs)
        return Response(json_encode(response_data.data))