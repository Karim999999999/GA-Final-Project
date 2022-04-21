# status gives us a list of possible response codes
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.response import Response
# Import this when adding error handling, provides a default response when data is not found
from rest_framework.exceptions import NotFound
from .models import *  # Import all our models as we're using them in these views
# Import all our serializers as we're using them in these views
from .serializers.common import *
from rest_framework.permissions import IsAuthenticated

# add coop and view all coop's
# http//localhost:8000/api/coops/

class CoopsCreateList(APIView):
  #list all Coops
  def get(self, request):
        
      coops = Coop.objects.all()

      # Serialize the authors to JSON by using an AuthorSerializer with the many=True flag
      serialized_coops = PopulatedCoopSerializerNoMembers(coops, many=True)

      # Return the serialized authors with a HTTP 200 status code
      return Response(data=serialized_coops.data, status=status.HTTP_200_OK)
  permission_classes = [IsAuthenticated, ]
  #create new Coops
  def post(self, request):

    request.data['owner'] = request.user.id
    
    coop_serializer = PopulatedCoopSerializerNoMembers(data=request.data)


    if coop_serializer.is_valid():

      coop_serializer.save()

      return Response(data=coop_serializer.data, status=status.HTTP_201_CREATED)
    
      return Response(data=coop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view, edit and delete coop by Id
# http//localhost:8000/api/coops/<int:pk>/
class CoopsViewEditDelte(APIView):
  #view detailed coop
  def get(self, request, pk):

      # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
      coop = self.get_coop(pk=pk)

      # Create a new serializer with the current author data - we're only returning one author so we don't need the many=True flag
      serialized_coop = PopulatedCoopSerializerWithMembers(coop)

      # Return the serialized author data and a HTTP 200 response
      return Response(data=serialized_coop.data, status=status.HTTP_200_OK)  
  #edit coop
  def post(self, request, pk):
    
        # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
        coop_to_update = self.get_coop(pk=pk)

        # Create a new serializer with the current author data and apply the changes from the incoming request data (updated author)
        # We specify the key `data` because we aren't adhering to the order of the arguments, same as `pk=pk` and `many=True`
        updated_coop = PopulatedCoopSerializerWithMembers(coop_to_update, data=request.data)

        # Check whether the updates are valid
        if updated_coop.is_valid():

            # Updates are valid so save them to the database
            updated_coop.save()

            # Data has been saved return a 200 response and the updated data
            return Response(updated_coop.data, status=status.HTTP_200_OK)

        # Incoming update is not valid so return a HTTP 400 bad request response
        return Response(data=updated_coop.errors, status=status.HTTP_400_BAD_REQUEST)
  #delete coop
  def delete(self, request, pk):
    # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
        coop_to_delete = self.get_coop(pk=pk)

        # Delete the author record
        coop_to_delete.delete()

        # Return a successful HTTP 204 response
        return Response(status=status.HTTP_204_NO_CONTENT)  
  
#internal function
def get_coop(self, pk):

        # Use a `try` here so if the code within it throws an exception it will be caught in the `except` block and handled rather than returning a HTTP 500 server error response code
        try:
            # Get the author from the database if it exists. If not, an Author.DoesNotExist error will be raised
            return Coop.objects.get(pk=pk)

        # Django Models have a DoesNotExist exception that occurs when a query returns no results
        # Link: https://docs.djangoproject.com/en/4.0/ref/models/class/#model-class-reference
        # Author.DoesNotExist errors are caught and handled here
        except Coop.DoesNotExist:

            # Raising a NotFound error will return a HTTP 404 response on the API. Further execution of the code will cease.
            # We'll also pass a custom message on the detail key so; the user knows what's wrong
            # NotFound returns a 404 response
            # Link: https://www.django-rest-framework.org/api-guide/exceptions/#notfound
            # Raise and return can both be used inside an exception, but NotFound has to be raised
            # Raising an exception is when you're indicating a specific behaviour or outcome like NotFound
            # Returning an exception is for something generic like Response above
            raise NotFound(detail="Can't find that Coop")
