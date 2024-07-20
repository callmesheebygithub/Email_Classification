from django.http import HttpResponse as hr
from django.shortcuts import render 

def homepage(request):
    try:
        if request.method=="POST":
            Email=request.POST.get("message")
            return hr(Email)
    except:
        pass
    return render (request,"homepage.html")

def about(request):
    return render (request,"about.html")

def contact(request):
    return render (request,"contact.html")

def service(request):
    return render (request,"service.html")