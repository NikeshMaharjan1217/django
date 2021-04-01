from django.contrib import admin

from .models import bus, ticket_purchased
# Register your models here.
admin.site.register(bus)
admin.site.register(ticket_purchased)