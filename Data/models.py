from django.db import models
from django.contrib.auth.models import User

class vaccinated(models.Model):
    name= models.CharField(max_length=128)
    adhar = models.IntegerField()
    mobile = models.IntegerField()
    dob = models.CharField(max_length = 30)
    pic = models.ImageField(upload_to = 'images/')
# Create your models here.
    def __str__(self):
        return self.name
