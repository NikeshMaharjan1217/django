from django.db import models

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=255)


