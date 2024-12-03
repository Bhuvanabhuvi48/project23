from django.shortcuts import render

# Create your views here.
def index(request):
    response=render(request,"app1/index1.html")
    return response
def display(request):
    sales_data={2010:4500,
                2011:5600,
                2012:6000,
                2013:7000,
                2014:8000}
    response=render(request,"app1/display.html",context={'sales_data':sales_data})
    return response
