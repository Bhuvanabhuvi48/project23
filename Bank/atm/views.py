from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deposit(request):
    output='''<html>
    <BODY bgcolor=pink>
    <h1>welcome to deposit view</h1>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response
def withdraw(request):
    output='''<HTML>
    <BODY bgcolor=yellow>
    <h2>this is withdraw view</h2>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response
def home(request):
    output='''<HTML>
    <BODY bgcolor=green>
    <h2>this is home page</h2>
    <a href=http://127.0.0.1:8000/deposit>DEPOSIT</a><br>
    <a href=http://127.0.0.1:8000/withdraw>WITHDRAW</a><br>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response