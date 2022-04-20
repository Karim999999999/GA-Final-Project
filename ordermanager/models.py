from django.db import models
from coopcreator.models import *
from coopmanager.models import *
import datetime
from jwt_auth.models import *

User = get_user_model()
class OrderProposalStatus(models.Model):
  status = models.CharField(max_length=100)
  status_description = models.CharField(max_length=100)

class OrderStatus(models.Model):
  status = models.CharField(max_length=100)
  status_description = models.CharField(max_length=100)

class OrderProposal(models.Model):
  coop_id = models.ForeignKey(Coop, related_name='shopping_list', on_delete=models.CASCADE)
  items_id = models.ManyToManyField(CoopItem, related_name='shopping_list')
  date_created = models.DateField(("Date"), default=datetime.date.today)
  deadline = models.DateField()
  delivery_day = models.DateField()
  order_proposal_status = models.ManyToManyField(OrderProposalStatus, related_name='orders')

class Order(models.Model):
  user_id = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
  order_proposal_id = models.ForeignKey(OrderProposal, related_name='orders', on_delete=models.CASCADE)
  order_status = models.ManyToManyField(OrderStatus, related_name='orders')