from django.urls import path
from .views import *

urlpatterns = [
  # add coop and view all coop's
  path('coops/', CoopsCreateList.as_view()),
  path('coops/owned/', CoopsCreateList.as_view()),
  # view, edit and delete coop by Id
  path('coops/<int:pk>/', CoopsViewEditDelte.as_view()),
  path('cities/', GetOperationalCities.as_view()),
  path('cooptags/', GetCoopTags.as_view()),
  path('purchase_options/', GetPurchaseOptions.as_view()),
]