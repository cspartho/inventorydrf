from .views import InventoryList,InventoryDetail
from django.urls import path

urlpatterns = [
    path('inventory/',InventoryList.as_view(),name='inventory_list'),
    path('inventory/<int:pk>/',InventoryDetail.as_view(),name="inventory_detail"),
]