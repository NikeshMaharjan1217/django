from django.urls import path

from . import views

app_name = 'bus'

urlpatterns = [
   
    path('',views.index, name='bus'),
    path('bus/',views.route, name='route'),
    path('show/',views.show, name='show'),
    path('delete/<int:pk>',views.delete, name='delete'),
    path('edit/<int:pk>',views.edit, name='edit'),
    path('updated/<int:pk>',views.update, name='update'),
    path('ticket/<int:pk>',views.ticket, name='ticket'),
    path('display/',views.display, name='display'),

]