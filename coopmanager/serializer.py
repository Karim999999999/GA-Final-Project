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

class PopulatedCoopItemSerializer(CoopItemSerializer):
  coop_id = PopulatedCoopSerializerNoMembers()
  item_type = ItemTypeSerializer()
  quantity_units = QuantityUnitSerializer()