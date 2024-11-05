# blog/views.py

from rest_framework import viewsets
from .models import Photo
from .serializers import PhotoSerializer
from django.shortcuts import render
from django.http import HttpResponse

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer



def show_received_file(request):
    try:
        with open('received_file.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = "No file received yet."

    return HttpResponse(f"<pre>{content}</pre>")