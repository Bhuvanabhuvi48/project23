from django.shortcuts import render
from app1.models import Bhuna2

# Create your views here.
def display_emp(request):
    qs=Bhuna2.objects.all()
    response=render(request,'app1/display.html',context={'qs':qs})
    return response
def view_emp(request):
    j=request.GET['job']
    if j!='all':
        qs=Bhuna2.objects.filter(job=j)
    else:
        qs=Bhuna2.objects.all()
    response=render(request,'app1/showemp.html',context={'qs':qs})
    return response
def display(request):
    response=render(request,"app1/index.html")
    return response

