from django.views.generic import ListView,DetailView
from .models import Inventory

class InventoryList(ListView):
    model = Inventory
    template_name = 'inventory/list.html'
    context_object_name = 'inventories'

class InventoryDetail(DetailView):
  model = Inventory
  template_name = 'inventory/detail.html'
  context_object_name = 'inventory'
