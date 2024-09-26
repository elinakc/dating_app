from rest_framework import serializers
from .models import CustomUser, Match, Message, UserPreferences, SwipeAction

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['id', 'username','email','gender','interested_in',
                 'location','profile_picture','date_of_birth']
        extra_kwargs ={'password':{'write_only':True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'user1', 'user2', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'attachment', 'timestamp', 'is_read']

class SwipeActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwipeAction
        fields = ['id', 'swiper', 'swiped', 'action', 'timestamp']

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = ['id', 'user', 'age_min', 'age_max', 'distance_max', 'show_me_on_app']
