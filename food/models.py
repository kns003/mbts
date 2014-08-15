from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 100)


    def __unicode__(self):
        return self.name
