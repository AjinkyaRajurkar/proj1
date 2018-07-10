from django.shortcuts import render
from django.http import HttpResponse
from .models import datatable2
def home(request):
    return render(request,"home.html")
def enterdetails(request):
    return render(request,"enterdetails.html")
def savedetails(request):
    roomid1=request.POST["r1"]
    food1=request.POST["t1"]
    trip1=request.POST["t2"]
    shopping1=request.POST["t3"]

    v=datatable2(roomid=roomid1,food=food1,trip=trip1,shopping=shopping1)
    v.save()

    return render(request,"home.html")
def calc(request):
    return render(request,"calexp.html")
def cal1(request):
     global c
     rid=request.POST["p1"]
     a=datatable2.objects.get(roomid=rid)
     food=a.food
     trip=a.trip
     shopping=a.shopping
     c=food+trip+shopping
     a={'food':food,'trip':trip,'shopping':shopping,'total':c}
     return render(request,"cal2.html",{'a':a})
def indvexp(request):
    participants=request.GET["t4"]
    pershare=int(c)/int(participants)
    return render(request,"output.html",{'pershare':pershare})
