from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is not matching")
            return redirect(request, 'signup.html')
             
        try:
            if User.objects.get(username=email):
                messages.info(request, "User exists with this email")
                return redirect(request, 'signup.html')
               
        
        except Exception as identifier:
            pass        
        
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject = "Activate your Account"
        message = render_to_string('activate.html', {
            'user' : user,
            'domain' : '127.0.0.1:8000',   # While hosting website you should change the domain name
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' :generate_token.make_token(user)
            
            
        })
        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER,
        [email])
        #email_message.send()                 # for email activation
        messages.success(request, "Activate Your account by clicking link provided in gmail")
        return redirect('authapp/login/')
                
    else:
        return render(request, "signup.html")
              
class ActivateAccountView(View):
    def get(self, request, uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user, token):
            user.is_active=True
            user.save()
            messages.info(request,"Account activated Successfully")
            return redirect('authapp/login')
        return render(request,"authapp/activatefail.html")        


def handlelogin(request):
    if request.method=="POST":
        
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username, password = userpassword)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successfull")
            return render(request, "index.html")
        
        else :
            messages.error(request, "Invalid credentials")
            return redirect('authapp/login')
        
        
    #return render(request,"login.html")



def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/authapp/login')
