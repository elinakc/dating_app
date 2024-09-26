from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import CustomUser, Message, Match, SwipeAction, UserPreferences
from core.serializers import CustomUserSerializers, MatchSerializer, MessageSerializer, SwipeActionSerializer, UserPreferenceSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    permission_classes = [IsAuthenticated]

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class SwipeActionViewSet(viewsets.ModelViewSet):
    queryset = SwipeAction.objects.all()
    serializer_class = SwipeActionSerializer
    permission_classes = [IsAuthenticated]

class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferenceSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView:
    pass