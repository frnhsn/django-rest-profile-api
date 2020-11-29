from django.urls import path, include
from .views import (
    HelloApiView, 
    HelloApiViewSet, 
    UserProfileViewSet, 
    LoginView,
    UserFeedViewset
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloApiViewSet, basename='hello-api-viewset')
router.register('user-profile', UserProfileViewSet, basename='user-profile')
router.register('user-feed', UserFeedViewset, basename='user-feed')

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
    path('login/', LoginView.as_view()),
    path('', include(router.urls))
]
