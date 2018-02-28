from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.http import HttpResponse

from .models import *
from .serializers import *
from util.CommonUtil import *
from util.AmazonUtil import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).list(request, *args, **kwargs)
        return Response(json_result(response_data.data, True))
    # create function already in serializers
    # def create(self, request, *args, **kwargs):
        # response_data = super(UserViewSet, self).create(request, *args, **kwargs)
        # return Response(json_result(response_data.data, True))
    def retrieve(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def update(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).update(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def destroy(self, request, *args, **kwargs):
        response_data = super(UserViewSet, self).destroy(request, *args, **kwargs)
        return Response(json_result(response_data.data))

    # get music by user /mp/api/user/{pk}/music/
    @detail_route(methods=['get'], url_path='music')
    def get_music_by_user(self, request, pk=None):
        music = Music.objects.filter(user=pk)
        serializer = MusicSerializer(music, many=True)
        if serializer.data:
            # if serializer.data > 0 return json_result
            return Response(json_result(serializer.data), status=status.HTTP_200_OK)
        else:
            # throw not found exceptions to display error result
            raise exceptions.NotFound()
        
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    
    def list(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).list(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def create(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).create(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def retrieve(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).retrieve(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def update(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).update(request, *args, **kwargs)
        return Response(json_result(response_data.data))
    def destroy(self, request, *args, **kwargs):
        response_data = super(MusicViewSet, self).destroy(request, *args, **kwargs)
        return Response(json_result(response_data.data))

def SendEmail(request):
    SENDER = "David Lo <davidlo.lyf@gmail.com>"
    RECIPIENT = "davidlo.lyf@gmail.com"
    SUBJECT = "Amazon SES Test (SDK for Python) - Edit By David Lo"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """            
    send_status = AmazonSES(SENDER,RECIPIENT,SUBJECT,BODY_TEXT,BODY_HTML).send()
    if send_status is True:
        return HttpResponse("OK");
    else:
        return HttpResponse("Fail");