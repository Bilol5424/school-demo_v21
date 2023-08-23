from rest_framework import serializers
from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('id',"phone","additional_number","email","working_mode","photo")