from django.shortcuts import render
from rest_framework import generics


from ..models import School
from ..serializer import SchoolSerializer


# Create your views here.
class SchoolList(generics.ListCreateAPIView):
  queryset = School.objects.all()
  serializer_class = SchoolSerializer


class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = School.objects.all()
  serializer_class = SchoolSerializer



class SchoolSearchByName(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return School.objects.filter(name=name)


class SchoolSearchByCategory(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return School.objects.filter(category=category)


class SchoolSearchByAddress(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        address = self.kwargs['address']
        return School.objects.filter(address=address)


