from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey('Supplier',related_name='supplier',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
