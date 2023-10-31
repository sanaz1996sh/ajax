from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def reg(request):
    if request.method=="POST":
        u=request.POST.get("username")
        f=request.POST.get("family")
        p=request.POST.get("password")
        p2=request.POST.get("password2")
        registercls.objects.create(username=u,family=f,password=p,password2=p2)
        return HttpResponse("مشخصات شما ثبت شد")
        

    return render (request,"register_app/register.html")
