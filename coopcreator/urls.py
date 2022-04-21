from django.urls import path
from .views import *

urlpatterns = [
  # add coop and view all coop's
  path('coops/', CoopsCreateList.as_view()),
  # view, edit and delete coop by Id
  path('coops/<int:pk>/', CoopsViewEditDelte.as_view()),
]