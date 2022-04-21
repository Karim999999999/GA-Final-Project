from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .serializers import *
from .views import * 
from coopcreator.views import get_coop

#view all existing order proposals for a Coop by Id, make a new order proposals
# http//localhost:8000/api/coops/<int:pk>/order_proposals/

class OrderProposalsListCreate(APIView):
  #View List of All of One Coops Order Proposals:
  def get(self, request, pk):
    coop_order_proposals = self.get_order_proposal_by_coop_id(pk=pk)
    serialized_coop_order_proposal = PopulatedOrderProposalSerializer(coop_order_proposals, many = True)
    return Response(data=serialized_coop_order_proposal.data, status=status.HTTP_200_OK)
  #Create New Order for Order Proposal For Coop:
  def post(self, request, pk):
    coop = self.get_coop(pk=pk)
    if coop.owner == request.user.id:
      request.data['coop_id'] = pk
      serialized_coop_order_proposal = OrderProposalSerializer(data=request.data)
      if serialized_coop_order_proposal.is_valid():
        serialized_coop_order_proposal.save()
        return Response(data=serialized_coop_order_proposal.data, status=status.HTTP_201_CREATED)
      return Response(data=serialized_coop_order_proposal.errors, status=status.HTTP_400_BAD_REQUEST)
    return(f'User {request.user.id} is the owner of the coop')

#view or delete  detailed order proposal by proposal id
# http//localhost:8000/api/coops/order_proposals/<int:pk>/
class OrderProposalViewEditDelete(APIView):
  #View Details of Single Order Proposal:
  def get(self, request, pk):
    order_proposal = self.get_order_proposal_by_id(pk=pk)
    serialized_order_proposal = PopulatedOrderProposalSerializer(order_proposal)
    return Response(data=serialized_order_proposal.data, status=status.HTTP_200_OK)
  #Edit Details of Single Order Proposal:
  def put(self, request, pk):
    order_proposals_to_update = self.get_order_proposal_by_id(pk=pk)
    updated_item = OrderProposalSerializer(order_proposals_to_update, data=request.data)
    if updated_item.is_valid():
        updated_item.save()
        return Response(updated_item.data, status=status.HTTP_200_OK)
    return Response(data=updated_item.errors, status=status.HTTP_400_BAD_REQUEST)
  #Delete Single Order Proposal:
  def delete(self, request, pk):
    order_proposal_to_delete = self.get_order_proposal_by_id(pk=pk)
    order_proposal_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#view all existing orders, make a new orders
# http//localhost:8000/api/coops/order_proposals/<int1:pk1>/orders/
class OrdersListCreate(APIView):
  #View List of All Orders of One Coops Order Proposals:
  def get(self, request, pk):
    orders = self.get_order_by_order_proposal_id(pk=pk)
    serialized_order = PopulatedOrderSerializer(orders, many = True)
    return Response(data=serialized_order.data, status=status.HTTP_200_OK)
  #Create Order Proposal For Coop
  def post(self, request, pk):
    request.data['user_id'] = request.user.id
    serialized_coop_order = OrderSerializer(data=request.data)
    if serialized_coop_order.is_valid():
      serialized_coop_order.save()
      return Response(data=serialized_coop_order.data, status=status.HTTP_201_CREATED)
    return Response(data=serialized_coop_order.errors, status=status.HTTP_400_BAD_REQUEST)


#view, edit or delete  detailed order  by order id
# http//localhost:8000/api/coops/order_proposals/orders/<int:pk>/
class OrderViewEditDelete(APIView):
  #View Details of Single Order:
  def get(self, request, pk):
    order = self.get_order_by_id(pk=pk)
    serialized_order = PopulatedOrderSerializer(order)
    return Response(data=serialized_order.data, status=status.HTTP_200_OK)
  #Edit Details of Single Order:
  def put(self, request, pk):
    order_to_update = self.get_order_by_id(pk=pk)
    updated_item = OrderSerializer(order_to_update, data=request.data)
    if updated_item.is_valid():
        updated_item.save()
        return Response(updated_item.data, status=status.HTTP_200_OK)
    return Response(data=updated_item.errors, status=status.HTTP_400_BAD_REQUEST)
  #Delete Single Order:
  def delete(self, request, pk):
    order_to_delete = self.get_order_by_id(pk=pk)
    order_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  #internal functions:
def get_order_proposal_by_coop_id(self, pk):
    try:
      return OrderProposal.objects.get(coop_id=pk)
    except OrderProposal.DoesNotExist:
      raise NotFound(detail="Can't find that Order Proposal")

def get_order_proposal_by_id(self, pk):
    try:
      return OrderProposal.objects.get(pk=pk)
    except OrderProposal.DoesNotExist:
      raise NotFound(detail="Can't find that Order Proposal")
def get_order_by_order_proposal_id(self, pk):
    try:
      return Order.objects.get(order_proposal_id=pk)
    except Order.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
def get_order_by_id(self, pk):
    try:
      return Order.objects.get(pk=pk)
    except Order.DoesNotExist:
      raise NotFound(detail="Can't find that Coop Item")
