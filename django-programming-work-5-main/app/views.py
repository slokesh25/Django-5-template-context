from django.shortcuts import render

# Create your views here.

def jinga_print(request):
    d={'Name':'vinoth','Age':22}
    return render(request,'jinga_print.html',context=d)
