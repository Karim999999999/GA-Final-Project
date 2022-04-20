from rest_framework import serializers
from .models import *
from jwt_auth.serializers import UserSerializer
from coopcreator.serializers.common import *

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ('__all__')

class QuantityUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityUnit
        fields = ('__all__')

class CoopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoopItem
        fields = ('__all__')

class PriceBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceBracket
        fields = ('__all__')

class PopulatedCoopItemSerializer(CoopItem):
  coop_id = PopulatedCoopSerializerNoMembers()
  item_type = ItemTypeSerializer()
  quantity_units = QuantityUnitSerializer()
  def order_price_brackets(self, instance):
    price_brackets = instance.price_brackets.order_by('quantity_units')
    return PriceBracketSerializer(price_brackets, many=True).data
  
  price_brackets = serializers.SerializerMethodField(method_name=order_price_brackets)
