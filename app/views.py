from django.shortcuts import render
from django.contrib.auth import login
from .forms import UserLoginForm,RegisterUser
from django.contrib.auth.models import User

def login_user(request):
    form = UserLoginForm
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request,user)    
            print('user logined')       
    
    return render(request,'app/login.html',{'form':form})



def register(request):
    form = RegisterUser
    if request.method =='POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            form.save()
            print('user created')
            
    
    return render(request,'app/register.html',{'form':form})


# for registering a uer in django noraml user 

def register_user(request):
    if request.method == 'POST':
        username_user = request.POST.get('username')
        password_user = request.POST.get('password1')
        password_user_2 = request.POST.get('password2')
        if password_user == password_user_2:

             user = User.objects.create_user(username = username_user, password =password_user)
             login(request,user)
             return redirect('/')
        return HttpResponse('Wrong password')

    return render(request,'account_app/register.html')
