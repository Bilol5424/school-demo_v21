from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField("название категории", max_length=50)
  description = models.TextField("описание")

  class Meta:
    verbose_name = "категория"
    verbose_name_plural = "категории"

  def __str__(self):
    return f"{self.title}"
