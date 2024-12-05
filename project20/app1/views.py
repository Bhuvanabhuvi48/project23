from django.shortcuts import render
from app1.models import Employers

# Create your views here.
def display_emp(request):
    qs=Employers.objects.all()
    response=render(request,'app1/display.html',context={'qs':qs})
    return response
def view_emp(request):
    j=request.GET['job']
    if j!='all':
        qs=Employers.objects.filter(job=j)
    else:
        qs=Employers.objects.all()

    response=render(request,'app1/showemp.html',context={'qs':qs})
    return response
    
def display_empjob(request):
    response=render(request,'app1/view.html')
    return response
def update_view(request):
    eno=int(request.GET['eno'])
    usal=float(request.GET['usal'])
    try:
        e=Employers.objects.get(empno=eno)
        e.sal=e.sal+usal
        e.save()
        response=render(request,'app1/updateemp.html',context={'msg':'salary updated'})
        return response
    except:
        response=render(request,'app1/updateemp.html',context={'msg':'invalid employee no'})
        return response

def display_update_template(request):
    response=render(request,'app1/updateemp.html')
    return response
def aggregation(request):
    tol_sal=Employers.objects.aggregate(Sum('sal'))['sal__sum']
    max_sal=Employers.objects.aggregate(Max('sal'))['sal__max']
    min_sal=Employers.objects.aggregate(Min('sal'))['sal__min']
    avg_sal=Employers.objects.aggregate(Avg('sal'))['sal__avg']
    tdict={'tol_sal':tol_sal,'max_sal':max_sal,'min_sal':min_sal,'avg_sal':avg_sal}
    response=render(request,'app1/aggregation.html',context={'tdict':tdict})
    return response