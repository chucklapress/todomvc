from django.shortcuts import render
from rest_framework import generics
from todo.models import ToDos
from todo.serializers import ToDosSerializer

# Create your views here.
class ToDosListAPIView(generics.ListCreateAPIView):
    queryset = ToDos.objects.all()
    serializer_class = ToDosSerializer

class ToDosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDos.objects.all()
    serializer_class = ToDosSerializer
