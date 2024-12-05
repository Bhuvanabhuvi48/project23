from django.shortcuts import render
from app1.forms import PersonForm
from django.http import HttpResponse

# Create your views here.
def person_view(request):
    if request.method=="GET":
        perform=PersonForm()
        response=render(request,'app1/person_temp.html',context={'perform':perform})
        return response
    
    elif request.method=="POST":
        perform=PersonForm(request.POST)
        if perform.is_valid():
            name=perform.cleaned_data['name']
            age=perform.cleaned_data['age']
            city=perform.cleaned_data['city']
            output=f'<h2>{name},{age},{city}</h2>'
            response=HttpResponse(output)
            return response
        else:
            response=render(request,'app1/person_temp.html',context={'perform':perform})
            return response        


       
    