from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
   
    path('',views.index, name='customer'),
    path('insert/',views.insert, name='insert'),
    path('show/',views.display, name='display'),
    path('book/',views.book, name='book'),
    path('list/',views.show, name='show'),
    # path('ticket/<int:pk>',views.ticket, name='ticket'),
    path('delete/<int:pk>',views.delete, name='delete'),

    
]