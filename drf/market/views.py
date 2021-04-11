from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Animal, Lot, Bid
from .serializers import (
    AnimalSerializer, AnimalGetSerializer,
    LotSerializer, LotGetSerializer, LotPatchSerializer,
    BidSerializer, BidGetSerializer
)


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return AnimalGetSerializer
        return AnimalSerializer


class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return LotGetSerializer
        if self.action == 'partial_update':
            return LotPatchSerializer
        return LotSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return BidGetSerializer
        return BidSerializer

    def list(self, request, *args, **kwargs):
        """
        Pass lot id to get specific lot bids
        """
        query = request.GET.get('query')
        if not query:
            data = list(Bid.objects.all().values())
        else:
            data = list(Bid.objects.filter(lot_id=query).values())
        return JsonResponse(data, safe=False)
