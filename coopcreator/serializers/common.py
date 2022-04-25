from rest_framework import serializers
from ..models import *
from jwt_auth.serializers import UserSerializer


class CoopTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoopTag
        fields = ('__all__')

class PurchaseFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseFrequencyOption
        fields = ('__all__')

class OperationalCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalCity
        fields = ('__all__')

class CoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coop
        fields = ('__all__')

class PopulatedCoopSerializerNoMembers(CoopSerializer):
  city = OperationalCitySerializer()
  owner = UserSerializer()
  coop_tag = CoopTagSerializer(many=True)
  purchase_frequency_option = PurchaseFrequencySerializer()

class PopulatedCoopSerializerWithMembers(PopulatedCoopSerializerNoMembers):
  coop_members = UserSerializer(many=True)

