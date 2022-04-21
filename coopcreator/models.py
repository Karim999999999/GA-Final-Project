import string
from webbrowser import Opera
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField
from jwt_auth.models import *
from jwt_auth.models import CustomUser

User = get_user_model()

class CoopTag(models.Model):
  tag_name = models.CharField(max_length=100)
  tag_description = models.TextField(blank=True, default='Text')
  def __str__(self):
      return self.tag_name

class PurchaseFrequencyOption(models.Model):
  option_name = models.CharField(max_length=100)
  length_days = models.IntegerField(null= True)
  opition_description = models.TextField(blank=True, default='Text')
  def __str__(self):
      return self.option_name

class OperationalCity(models.Model):
  city_name = models.CharField(max_length=100)
  def __str__(self):
      return self.city_name

class Coop(models.Model):
  coop_name = models.CharField(max_length=200)
  coop_description = models.TextField()
  address_1 = models.CharField(max_length=200, null= True)
  address_2 = models.CharField(max_length=200, null= True)
  city = models.ForeignKey(OperationalCity, related_name='coop', on_delete=models.CASCADE, null=True)
  postcode = models.CharField(max_length=9)
  management_fee = models.IntegerField(null= True)
  bring_your_own_bag = models.BooleanField(default= True)
  owner = models.ForeignKey(User, related_name='owned_coop', on_delete=models.CASCADE)
  coop_tag = models.ManyToManyField(CoopTag, related_name='coop', blank=False)
  coop_members = models.ManyToManyField(CustomUser, related_name='joined_coop')
  purchase_frequency_option = models.ForeignKey(PurchaseFrequencyOption, related_name='coop', null=True, on_delete=models.CASCADE)
  def __str__(self):
      return self.coop_name  