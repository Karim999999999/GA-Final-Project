from rest_framework import serializers
from .models import *
from coopmanager.serializer import *
from coopcreator.serializers.common import *
from jwt_auth.serializers import UserSerializer


class OrderProposalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProposalStatus
        fields = ('__all__')

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityUnit
        fields = ('__all__')

class OrderProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProposal
        fields = ('__all__')

class PopulatedOrderProposalSerializer(OrderProposalSerializer):
  coop_id = PopulatedCoopSerializerNoMembers()
  def order_items_in_order(self, instance):
    items_id = instance.items_id.order_by('item_name')
    return PopulatedCoopItemSerializer(items_id, many=True).data
  items_id = serializers.SerializerMethodField(method_name=order_items_in_order)
  order_proposal_status = OrderProposalStatusSerializer(many=True)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class PopulatedOrderSerializer(OrderSerializer):
  user_id = UserSerializer()
  order_proposal_id = PopulatedOrderProposalSerializer()
  order_status = OrderStatusSerializer(many=True)


