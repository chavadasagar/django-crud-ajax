
import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import course,std
# Create your views here.


def savestd(request):

    std_name = request.POST.get('name')
    std_email = request.POST.get('email')
    std_course = request.POST.get('course')
    std_gender = request.POST.get('gender')
    std_dob = request.POST.get('dob')
    
    s = std(name=std_name,gender=std_gender,dob=std_dob,c_name=std_course,email=std_email)
    s.save()

    return redirect('home')

def deletestd(request):
    s_id = request.GET.get('id')

    std.objects.get(id=s_id).delete()

    return redirect('home')

def update(request):
    
    sid = request.POST.get('sid')
    std_name = request.POST.get('name')
    std_email = request.POST.get('email')
    std_course = request.POST.get('course')
    std_gender = request.POST.get('gender')
    std_dob = request.POST.get('dob')
    
    s = std(id=sid,name=std_name,gender=std_gender,dob=std_dob,c_name=std_course,email=std_email)
    s.save()
    return redirect('home')

def updatestd(request):

    sid = request.GET.get('id')
    return render(request,'update.html',{'std':std.objects.get(id=sid),"course":course.objects.all()})


def home(request):
    return render(request,'index.html',{"course":course.objects.all()})

def showallstd(request):
    return render(request,'showall.html',{'allstd':std.objects.all(),"course":course.objects.all()})