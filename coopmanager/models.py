from django.db import models
from coopcreator.models import Coop

class ItemType(models.Model):
  item_type = models.CharField(max_length=100)  
  item_description = models.TextField()

class QuantityUnit(models.Model):
  quantity_unit_full = models.CharField(max_length=100)
  quantity_unit_shorthand = models.CharField(max_length=100)
  quantity_unit_description = models.TextField()

class CoopItem(models.Model):
  coop_id = models.ForeignKey(Coop, related_name='coop',  on_delete=models.CASCADE)
  item_name = models.CharField(max_length=200)
  item_type = models.ForeignKey(ItemType, related_name='item', on_delete=models.CASCADE)
  item_description = models.TextField()
  minimum_purchase_amount = models.IntegerField()
  item_url = models.CharField(max_length=300)
  quantity_units = models.ForeignKey(QuantityUnit, related_name='item', on_delete=models.CASCADE)

class PriceBracket(models.Model):
  coop_item_id = models.ForeignKey(CoopItem, related_name='price_brackets',  on_delete=models.CASCADE)
  quantity = models.IntegerField()
  quantity_price = models.IntegerField()