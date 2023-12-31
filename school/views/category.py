from django.shortcuts import render
from rest_framework import generics


from ..models import Category
from ..serializer import CategorySerializer


# Create your views here.
class CategoryList(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
