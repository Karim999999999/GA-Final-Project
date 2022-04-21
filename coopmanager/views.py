from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework.exceptions import NotFound
from .models import *
from coopcreator.views import get_coop
# Create your views here.

# view and add coop items to a coop id 
# http//localhost:8000/api/coops/<int:pk>/items
class CoopItemListCreate(APIView):
  #View Coop Items for one Coop:
  def get(self, request, pk):
    coop_items = self.get_item_by_coop_id(pk=pk)
    serialized_coop_item = PopulatedCoopItemSerializer(coop_items, many = True)
    return Response(data=serialized_coop_item.data, status=status.HTTP_200_OK)
  #Create Coop Item for a coop:
  def post(self, request, pk):
    coop = self.get_coop(pk=pk)
    if coop.owner == request.user.id:
      request.data['coop_id'] = pk
      coop_item_serializer = CoopItemSerializer(data=request.data)
      if coop_item_serializer.is_valid():
        coop_item_serializer.save()
        return Response(data=coop_item_serializer.data, status=status.HTTP_201_CREATED)
      return Response(data=coop_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=f'User {request.user.id} is the owner of the coop', status=403)

# change, detail view and delete a coop item tied to a specific coop id
# http//localhost:8000/api/coops/items/<int:pk>/
class CoopItemEditViewDelete(APIView):
  #View Coop Item:  
  def get(self, request, pk):
    coop_item = self.get_item_by_id(pk=pk)
    serialized_coop_item = PopulatedCoopItemSerializer(coop_item)
    return Response(data=serialized_coop_item.data, status=status.HTTP_200_OK)
  #Edit Coop Item:
  def put(self, request, pk):
    item_to_update = self.get_item_by_id(pk=pk)
    updated_item = PopulatedCoopItemSerializer(item_to_update, data=request.data)
    if updated_item.is_valid():
        updated_item.save()
        return Response(updated_item.data, status=status.HTTP_200_OK)
    return Response(data=updated_item.errors, status=status.HTTP_400_BAD_REQUEST)
  #Delete Coop Item:
  def delete(self, request, pk):
      coop_item_to_delete = self.get_item_by_id(pk=pk)
      coop_item_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

# add and view price brackets to a coop item by coop item id 
# http//localhost:8000/api/coops/items/<int:pk>/price_bracket/
class CoopItemPriceBracketListCreate(APIView):
  #View Coop Items Price Bracket List:
  def get(self, request, pk):
    price_brackets= self.get_price_brackets_by_item_id(pk=pk)
    serialized_price_bracket = PriceBracketSerializer(price_brackets, many = True)
    return Response(data=serialized_price_bracket.data, status=status.HTTP_200_OK)
  #Create Coop Items Price Bracket:
  def post(self, request, pk):
      request.data['item_id'] = pk
      price_backet_serializer = PriceBracketSerializer(data=request.data)
      if price_backet_serializer.is_valid():
        price_backet_serializer.save()
        return Response(data=price_backet_serializer.data, status=status.HTTP_201_CREATED)
      return Response(data=price_backet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete, and edit a price bracket for a coop item  by coop item id
# http//localhost:8000/api/coops/items/price_bracket/<int:pk>/
class CoopItemPriceBracketEditViewDelete(APIView):
  #View Single Coop Item Price Bracket List:
  def get(self, request, pk):
    price_bracket = self.get_price_bracket_by_id(pk=pk)
    serialized_price_bracket = PriceBracketSerializer(price_bracket)
    return Response(data=serialized_price_bracket.data, status=status.HTTP_200_OK)
  #Edit Coop Item Price Bracket:
  def put(self, request, pk):
    price_bracket_to_update = self.get_price_bracket_by_id(pk=pk)
    updated_price_bracket = PriceBracketSerializer(price_bracket_to_update, data=request.data)
    if updated_price_bracket.is_valid():
        updated_price_bracket.save()
        return Response(updated_price_bracket.data, status=status.HTTP_200_OK)
    return Response(data=updated_price_bracket.errors, status=status.HTTP_400_BAD_REQUEST)
  #Delete Coop Item Price Bracket:
  def delete(self, request, pk):
      price_bracket_to_delete = self.get_price_bracket_by_id(pk=pk)
      price_bracket_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

  #internal functions:
def get_item_by_coop_id(self, pk):
    try:
      return CoopItem.objects.get(coop_id=pk)
    except CoopItem.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
def get_item_by_id(self, pk):
    try:
      return CoopItem.objects.get(pk=pk)
    except CoopItem.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
def get_price_brackets_by_item_id(self, pk):
    try:
      return PriceBracket.objects.get(coop_item_id=pk)
    except PriceBracket.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
def get_price_bracket_by_id(self, pk):
    try:
      return PriceBracket.objects.get(pk=pk)
    except PriceBracket.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
