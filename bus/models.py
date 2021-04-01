from django.db import models
from django.db.models.deletion import CASCADE

from customer.models import customer
from datetime import datetime

# Create your models here.
class bus(models.Model):
    
    bus_route = models.CharField(max_length = 255)
    bus_time = models.TimeField()
    bus_ticket = models.IntegerField(default=0)



class ticket_purchased(models.Model):
    purchased_date = models.DateTimeField(auto_now_add=True)
    purchased_by = models.ForeignKey(customer,on_delete=models.CASCADE)
    bus_route = models.ForeignKey(bus,on_delete=models.CASCADE)
    bus_time =models.TimeField()
    ticket_rate = models.IntegerField(default=0)
    ticket_quantity = models.IntegerField(default=0)
    ticket_price = models.IntegerField(default=0)


