from rest_framework import serializers
from .models import UserProfile, UserFeed


class HelloSerializer(serializers.Serializer):
    """ Serialize a name field for testing API view """

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serialize a user profile object """

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_style': 'password'}
            }
        }

class UserFeedSerializer(serializers.ModelSerializer):
    """ Serialize a user profile object """

    class Meta:
        model = UserFeed
        fields = ['user', 'status_text', 'created_at']
        read_only_fields = ['user']

        


