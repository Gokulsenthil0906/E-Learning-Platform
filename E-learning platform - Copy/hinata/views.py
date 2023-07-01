from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def log_in(request):
   if request.user.is_authenticated:
        return redirect('home/')
   else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home/')
            else:
                messages.info(request, "Username or password is incorrect")
        return render(request, 'login.html')        

def log_out(request):
    logout(request)
    return redirect('login')
@login_required(login_url="login")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="login")
def ml(request):
    return render(request,'ml.html')
    
@login_required(login_url="login")
def ds(request):
    return render(request,'ds.html') 
  
@login_required(login_url="login")
def web(request):
    return render(request,'web.html')
    
@login_required(login_url="login")
def mlquiz(request):
    return render(request,'ml quiz.html')
    
@login_required(login_url="login")
def dsquiz(request):
    return render(request,'ds quiz.html')
 
@login_required(login_url="login")
def webquiz(request):
    return render (request,'web quiz.html')

@login_required(login_url="login")
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def chat(request):
    return render(request,'chat.html')

@login_required(login_url='login')
def Courses(request):
    return render(request,'coruse.html')

@login_required(login_url='login')
def handle(request,exception):
    return render(request,'404.html')

@login_required(login_url='login')
def codeeditor(request):
    return render(request,'code editor.html')

"""Courses section"""


@login_required(login_url='login')
def Ai(request):
    return render(request,'Courses/ai.html')

@login_required(login_url='login')
def cloud(request):
    return render(request,'Courses/cloud.html')

@login_required(login_url='login')
def python(request):
    return render(request,'Courses/python.html')

@login_required(login_url='login')
def c(request):
    return render(request,'Courses/C.html')

@login_required(login_url='login')
def cpp(request):
    return render(request,'Courses/C++.html')

@login_required(login_url='login')
def java(request):
    return render(request,'Courses/java.html')

@login_required(login_url='login')
def javascript(request):
    return render(request,'Courses/javascript.html')

@login_required(login_url='login')
def r(request):
    return render(request,'Courses/R.html')

#chat

