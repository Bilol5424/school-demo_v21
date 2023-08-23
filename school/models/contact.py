from django.db import models

# Create your models here.

class Contact(models.Model):
  phone= models.CharField("номер телефона",max_length=12)
  additional_number = models.CharField("доп.номер", max_length=12)
  email = models.EmailField("почта")
  working_mode = models.CharField("режим работы",max_length=25)
  photo = models.ImageField("фотография", upload_to='images/')

  class Meta:
    verbose_name = "Контакт"
    verbose_name_plural = "Контакты"

  def __str__(self):
    return f"{self.phone}"
