from django.shortcuts import render
from app1.models import Marks

# Create your views here.
def home(request):
    response=render(request,'app1/index.html')
    return response
def add_student_template(request):
    response=render(request,'app1/add_studentmarks.html')
    return response
def add_students(request):
    rno=int(request.GET['rno'])
    name=request.GET['name']
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    m=Marks(rollno=rno,name=name,sub1=s1,sub2=s2)
    m.save()
    response=render(request,'app1/add_studentmarks.html',context={'msg':'student added'})
    return response
def update_student_template(request):
    response=render(request,'app1/update_student.html')
    return response
def update(request):
    rno=int(request.GET['rno'])
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2']) 
    try:
        stud=Marks.objects.get(rollno=rno)
        stud.sub1=s1
        stud.sub2=s2
        stud.save()
        response=render(request,'app1/update_student.html',context={'msg':'student marks updated successfully'})
    except:
        response=render(request,'app1/update_student.html',context={'msg':'invalid student number try again'})
    return response
        
