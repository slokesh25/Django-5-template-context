from django.shortcuts import render

# Create your views here.

def app1(request):
    return render(request,'app1.html')

def app3(request):
    return render(request,'app3.html')