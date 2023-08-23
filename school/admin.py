from django.contrib import admin
from .models import Contact,Category,Hospital
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("title", "description")
  search_fields = ("title",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ("phone", "additional_number", "email", "working_mode", "photo")
  search_fields = ("phone",)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "address","city","contact")
  
