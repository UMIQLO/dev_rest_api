from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# test http request
def testHttp(request):
    return HttpResponse('This is HTTP Response (Debug)')
# test json request
def testJson(request):
    return JsonResponse({'debug':'This is JSON Response (Debug)'})