from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    secrets = serializers.HyperlinkedRelatedField(many=True, view_name='secret-detail', read_only=True)
 
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'secrets')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SecretSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Secret
        fields = ('url', 'secret', 'user')
