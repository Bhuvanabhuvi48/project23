from django.shortcuts import render

# Create your views here.
def list_students(request):
    student_list={101:["virat","python","virat.jpg"],
                  102:["boomra","java","boomra.jpg"],
                  103:["dhoni","c++","dhoni.jpg"],
                  104:["dhonivirat","django","dhonivirat.jpg"],
                  105:["ravindra","html","ravindra.jpg"]}
    response=render(request,"app1/student.html",context={'student_list':student_list})
    return response