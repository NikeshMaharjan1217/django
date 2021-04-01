from django.shortcuts import render, redirect
from django.urls import reverse
from .models import bus, ticket_purchased
from django.http import HttpResponse
from customer.models import customer
# Create your views here.
def index(request):
    return render (request, 'bus.html')


def route(request):
    route = request.GET['bus_route']
    time = request.GET['bus_time']
    ticket = request.GET['bus_ticket']
    save_data = bus(bus_route=route,bus_time=time, bus_ticket=ticket)
    save_data.save()
    return redirect(reverse('bus:show'))

def show(request):
    data=bus.objects.all()
    context= {'dis': data}
    return render(request,'display.html',context)

def edit(request,pk):
    bu = bus.objects.filter(id=pk)
    context= {'b':bu}
    return render(request,'update.html',context)


def update(request,pk):
    route = request.GET['bus_route']
    time = request.GET['bus_time']
    ticket = request.GET['bus_ticket']
    r = bus.objects.get(id=pk)
    r.bus_route = route
    r.bus_time = time
    r.bus_ticket = ticket
    r.save()
    return redirect(reverse('bus:show'))

def delete(request,pk):
    bu = bus.objects.get(id=pk)
    bu.delete()
    return redirect (reverse('bus:show'))


def ticket(request,pk):
    route= bus.objects.get(id=pk)
    time = request.GET['time']
    rate = int(request.GET['ticket'])
    a = request.GET['name']
    user = customer.objects.get(customer_name=a)
    quantity = int(request.GET['quantity'])
    total=rate*quantity
    store= ticket_purchased(purchased_by = user,bus_route = route,bus_time = time,ticket_rate = rate,ticket_quantity = quantity,ticket_price=total)
    store.save()
    return redirect(reverse('bus:display'))


def display(request):
    data=ticket_purchased.objects.all()
    print("hello")
    context= {'dis': data}
    return render(request,'dis.html',context)