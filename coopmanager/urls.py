from django.urls import path
from .views import *

urlpatterns = [
# view and add coop items to a coop id 
  path('coops/<int:pk>/items/', CoopItemListCreate.as_view()),
# change, detail view and delete a coop item tied to a specific coop id
  path('coops/items/<int:pk>/', CoopItemEditViewDelete.as_view()),
# add and view price brackets to a coop item by coop item id 
  path('coops/items/<int:pk>/price_bracket/', CoopItemPriceBracketListCreate.as_view()),
# delete, and edit a price bracket for a coop item  by coop item id
  path('coops/items/price_bracket/<int:pk>/', CoopItemPriceBracketEditViewDelete.as_view()),
  path('quantity_units/', GetQuantityUnits.as_view()),
  path('coop_item_types/', GetItemTypes.as_view()),
]