from rest_framework import viewsets, status

from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    
    @list_route(methods=['get'])
    def raw_sql_query(self, request):
        id = request.query_params.get('music', None)
        music = fun_raw_sql_query(music=id)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)