from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    response=render(request,'app1/login.html')
    return response
def login_view(request):
    uname=request.GET['user']
    response=render(request,"app1/inbox.html")
    response.set_cookie("uname",uname)
    return response
def inbox_view(request):
    uname=request.COOKIES['uname']
    output=f'''
<h2>{uname}</h2>
<h2>this is your inbox</h2>'''
    response=HttpResponse(output)
    return response

    

