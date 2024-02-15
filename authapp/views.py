from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.



def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')
        
        if password != confirm_password:
            messages.warning(request, "Password does not match")
            return redirect('/authapp/signup/')
        
        try:
            user = User.objects.get(email=email) 
            messages.info(request, "User with this email already exists. Please log in or reset your password.")
            return redirect('/authapp/login/')
        except User.DoesNotExist:
            pass
        
        user = User.objects.create_user(email=email, password=password) 
        user.save()
        
        messages.success(request, "Account created successfully. Please check your email for activation instructions.")
        return redirect('/authapp/login/') 
    
    return render(request, "signup.html")




def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        userpassword = request.POST.get('pass1')
        myuser=authenticate(request, username=username, password = userpassword) 
        print(myuser)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successfull")
            return render(request, "index.html")  
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')
    

 



def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/authapp/login')
