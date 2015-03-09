from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, GroupSerializer, SecretSerializer
from .models import Secret
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
@api_view(('GET',))
def api_root(request, format=None):
    """
    Returns the links for seeing all users and all secrets for the logged in user
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'secrets': reverse('secret-list', request=request, format=format)
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    Generates views for viewing the list of users and the details for a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SecretListCreate(generics.ListCreateAPIView):
    """
    A view for viewing the list of secrets for the logged in user
    """
    permission_classes = (IsOwner,)
    serializer_class = SecretSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous():
            return []
        else:
            return Secret.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SecretDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for viewing a specific secret
    """
    queryset = Secret.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = SecretSerializer
