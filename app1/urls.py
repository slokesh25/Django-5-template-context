from django.urls import path
from app1.views import *
app_name='anything'

urlpatterns=[
    path('app1/',app1,name='app1'),
    path('app3/',app3,name='app3'),
    
]