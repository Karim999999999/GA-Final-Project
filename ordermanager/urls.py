from django.urls import path
from .views import *

urlpatterns = [
# view and add coop items to a coop id 
  path('coops/<int:pk>/order_proposals/', OrderProposalsListCreate.as_view()),
# change, detail view and delete a coop item tied to a specific coop id
  path('coops/order_proposals/<int:pk>/', OrderProposalViewEditDelete.as_view()),
# add and view price brackets to a coop item by coop item id 
  path('coops/order_proposals/<int:pk>/orders/', OrdersListCreate.as_view()),
# delete, and edit a price bracket for a coop item  by coop item id
  path('coops/order_proposals/orders/<int:pk>/', OrderViewEditDelete.as_view()),
]