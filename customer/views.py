from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import customer
from bus.models import bus
from django.urls import reverse
# Create your views here.
def index(request):
    return render (request, 'customer.html')

def insert(request):
    name = request.GET['customer_name']
    name_save = customer(customer_name= name)
    name_save.save()
    
    return HttpResponse("Saved!")

def display(request):
    dispaly= bus.objects.all()
    user = customer.objects.all()
    context= {'dis': dispaly,'use':user}
    return render(request,'show.html',context)

def book(request):
    bu = bus.objects.filter(pk=request.GET['bus_id'])
    a = request.GET['tic']
   
    user = customer.objects.get(pk=a)
    context={'b': bu,'u': user}
    return render(request,'bill.html',context)


def show(request):
    user = customer.objects.all()
    context = {'users':user}
    return render(request,'u_list.html',context)

# def ticket(request):
#     user = customer.objects.all()
#     context = {'use':user}
#     return render(request,'show.html',context)

def delete(request,pk):
    dele = customer.objects.get(id=pk)
    dele.delete()
    return redirect (reverse('customer:show'))



    
