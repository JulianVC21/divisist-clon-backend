from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import User, Student

# Create your views here.


def index(request):
    data = {
        "message": "Holaaa"
    }
    return JsonResponse(data)
