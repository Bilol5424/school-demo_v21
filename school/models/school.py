from django.db import models

# Create your models here.

class School(models.Model):
  name = models.CharField("имя school",max_length=50)
  description = models.TextField("описание")
  address = models.CharField("Адрес", max_length=80)
  city = models.CharField("Город", max_length=50)
  category = models.ManyToManyField(
      "school.category",  related_name="school")
  contact = models.OneToOneField("school.contact", on_delete=models.CASCADE )

  class Meta:
    verbose_name = "school"
    verbose_name_plural = "schools"

  def __str__(self): 
    return f"{self.name}"

