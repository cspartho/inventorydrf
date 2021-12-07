from .views import InventoryList
from django.urls import path

urlpatterns = [
    path('inventory/',InventoryList.as_view(),name='list'),
]