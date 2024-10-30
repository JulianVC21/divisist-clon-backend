from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

# Create your views here.

def hello(request):
    return HttpResponse('Welcome to divisist backend app')

def test(req):
    return JsonResponse({'message': 'esto es un test'})

def getUsers(req):
    users = list(models.User.objects.all())
    print(users[0])
    return JsonResponse({
        'users': ''
    })
