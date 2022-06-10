from django.shortcuts import render
from .models import Book
from .serializers import BookSerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ListBook(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class DetailBook(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers