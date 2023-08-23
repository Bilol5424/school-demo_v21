from django.shortcuts import render
from rest_framework import generics


from ..models import Contact
from ..serializer import ContactSerializer


# Create your views here.
class ContactList(generics.ListCreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
