from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from .models import Student,Course
from .forms import StudentForm
from .forms import RegisterForm


# Create your views here.
# def home(request):
#     return HttpResponse("welcome to the home page")
# def about(request):
#     return HttpResponse("this is the about page for students")
# def contact(request):
#     return HttpResponse("<h1>contact page</h1><p>phone:123-456-789") 
# def greet(request):
#     return HttpResponse("hello everyone!...")

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def profile(request):
    context={
        "title":"welcome san!",
        "msg":"this is dynamic content from django."
    }
    return render(request,"profile.html",context)
def feedback(request):
    return render(request,"feedback.html")
def gallery(request):
    return render(request,"gallery.html")

def list_students(request):
    data = Student.objects.all()
    return render(request,"list_students.html",{"students":data})

def students_list(request):
    data = Student.objects.all()
    return render(request,"students_list.html",{"students":data})

def add_students(request):
    if request.method == "POST":
        form = StudentForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form =StudentForm()
    return render(request,"add_students.html",{"form":form}) 

def edit_students(request,id):
    students =get_object_or_404(Student,id=id)
    if request.method =="POST":
        form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form =StudentForm(instance=students)  
    return render(request,"edit_students.html",{"form":form}) 

def delete_students(request,id):
    students=get_object_or_404(Student,id=id)
    students.delete()
    return redirect('/students/')

def course_list(request):
    data=Course.objects.all()
    return render(request,"course_list.html",{"course":data})

def register_user(request):
    if request.method=="POST":
        form=register_user(request.POST)
        form.save()
        return redirect('/login/') 
    else:
         form=RegisterForm()
         return render(request,"register.html",{"form".form})

def login_user(request):
    if request.method=="POST":
       form=AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           username=form.cleaned_data.get("username")
           password=form.cleaned_data.get("password")
           User=authenticate(Usernamer=username,password=password)
           if User:
             login(request,User)
             return redirect('/dashboars')
    else:
            form=AuthenticationForm()
            return render(request,"login button")
    return render(request,"login.html",{"form":form})
        
def logout_user(request):
    logout(request)
    return redirect('/login/')  

@login_required(login_url="/login/")
def dashboard(request):
    return render(request,"dashboard.html")

def active_course(request):
    course = Course.objects.filter(active=True)
    return render(request, "active_course.html", {"courses": course}) 