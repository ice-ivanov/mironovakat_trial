from .views import AnimalViewSet, LotViewSet, BidViewSet
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('animals', AnimalViewSet)
router.register('lots', LotViewSet)
router.register('bids', BidViewSet)

app_name = 'market'
urlpatterns = [
    path('', include(router.urls)),
]
