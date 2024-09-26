from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, MatchViewSet, MessageViewSet, SwipeActionViewSet, UserPreferencesViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'swipes', SwipeActionViewSet)
router.register(r'preferences', UserPreferencesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]