from django.db import models
# from .models import dummy_table
# Create your models here.
class dummy_table(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()




