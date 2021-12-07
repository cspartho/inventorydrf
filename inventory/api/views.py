from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.filters import SearchFilter

from ..models import Inventory
from .serializers import InventoryDetailSerialzer, InventoryListSerialzer


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerialzer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

