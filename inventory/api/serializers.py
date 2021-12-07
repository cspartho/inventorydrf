from rest_framework import serializers
from ..models import Inventory,Supplier

class InventoryListSerialzer(serializers.ModelSerializer):
    supplier =serializers.StringRelatedField()
    class Meta:
        model = Inventory
        fields = ['name','supplier','availability']

class InventoryDetailSerialzer(serializers.ModelSerializer):
    supplier =serializers.StringRelatedField()
    class Meta:
        model = Inventory
        fields = ["name","description","note","stock","availability","supplier"]