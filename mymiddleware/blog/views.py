from django.shortcuts import render,HttpResponse

def home(requset):
    print("i am insdie the view function Home")
    return HttpResponse("This is home page")

# Create your views here.

def excep(request):
    a = 10/0    # this is use to arrise the exception
    return HttpResponse("I am exception views")