from django.db import models
from django.contrib.auth.models import AbstractUser
# from coopcreator.models import OperationalCity

class CustomUser(AbstractUser):
  image = models.CharField(max_length=200)
  address_1 = models.CharField(max_length=200, null= True)
  address_2 = models.CharField(max_length=200, null= True)
  city = models.ForeignKey('coopcreator.OperationalCity', related_name='user', on_delete=models.SET_NULL , null=True)
  postcode = models.CharField(max_length=9, null = True)
  # household_size = models.IntegerChoices()