from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

 
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Warehouse(models.Model):
    wh_x = models.IntegerField()
    wh_y = models.IntegerField()

    class Meta:
        unique_together = (('wh_x', 'wh_y'),)

class Order(models.Model):
    amazon_account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    truck_id = models.IntegerField(blank=True, null=True)
    ups_account = models.CharField(max_length=100, blank=True)
    status  = models.CharField(max_length=500, default ="status")
    destination_x = models.IntegerField()
    destination_y = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    time_created = models.DateTimeField(auto_now_add=True)
    time_packed = models.DateTimeField(blank=True, null=True)
    time_loaded = models.DateTimeField(blank=True, null=True)
    time_delivered = models.DateTimeField(blank=True, null=True)

class Cart(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = (('account', 'product'),)
    def __str__(self):
        return self.account.username + ' ' + self.product.name + ' ' + str(self.quantity) 
    
class Package(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    
    class Meta:
        unique_together = (('order', 'product'),)
    
class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    class Meta:
        unique_together = (('warehouse', 'product'),)