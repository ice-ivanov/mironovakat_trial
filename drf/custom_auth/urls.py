from .views import UserViewSet
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)

app_name = 'auth'
urlpatterns = [
    path('', include(router.urls)),
]
