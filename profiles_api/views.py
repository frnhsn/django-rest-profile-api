from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.permissions import BasePermission, IsAuthenticated

from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import HelloSerializer, UserProfileSerializer, UserFeedSerializer

from .models import UserProfile, UserFeed

from .permissions import UpdateOwnProfile, UpdateOwnFeed

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView features """

        return Response({'message': 'Hello'})

    def post(self, request):
        
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            name    = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            

class HelloApiViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    def list(self, request):
        """ Return hello message """

        return Response({
            "message": "Hello"
        })

class UserProfileViewSet(viewsets.ModelViewSet):
    """ User profile viewset """

    serializer_class        = UserProfileSerializer
    queryset                = UserProfile.objects.all()
    authentication_classes  = [TokenAuthentication]
    permission_classes      = [UpdateOwnProfile]
    filter_backends         = [filters.SearchFilter]
    search_fields           = ['name', 'email']


class LoginView(ObtainAuthToken):
    """ Login view """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserFeedViewset(viewsets.ModelViewSet):
    """ User feed view """
    
    serializer_class = UserFeedSerializer
    queryset = UserFeed.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated&UpdateOwnFeed]

    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        serializer.save(user=self.request.user)

