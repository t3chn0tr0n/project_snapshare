from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from . import pyfunctions
from .models import Temp_user


# def signup(request):

#     current_site = get_current_site(request)
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         if request.method == 'POST':
#             if request.POST['password1'] == request.POST['password2']:
#                 try:
#                     user = Temp_user.objects.get(username=request.POST['username'])
#                     return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
#                 except User.DoesNotExist:
#                     token = pyfunctions.generate_url()
#                     user = Temp_user.objects.create(uname=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], token=token)

#                     reciever = ['avikmukherjee1908@gmal.com']
#                     url = "http://localhost:8000/accounts/validate/" + token
    
#                     if pyfunctions.varification_mailto(reciever, url):
                        
#                         responce = "<h2> Email Sent <br /> Please Varify you email! </h2>"
#                     else:
#                         responce = "<h1> ERROR! mail not sent </h1>" 
    
#                     return HttpResponse(responce)
#             else:
#                 return render(request, 'accounts/signup.html', {'title':'signup', 'error':'Passwords must match'})
#         else:
#             return render(request, 'accounts/signup.html', {'title':'signup'})


def login(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    else:
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                return render(request, 'accounts/login.html',{"title":"log in", 'error':'username or password is incorrect.'})
        else:
            return render(request, 'accounts/login.html', {"title":"log in"})


def  logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            
            #-1. form validation
            #-2. save data in local table (if not already there, in both user tables)
                #i. generate token
                #ii. send email
                #iii. show Email sent page
            #-3. if username exists, show an error page

            # validations:
            # =============
            # if not form.is_valid():
            #     error = "Invalid Form details!"
            error = ""
            
            if request.POST["password1"] != request.POST["password2"]:
                error = "Password must match!"
            elif Temp_user.objects.filter(uname = request.POST["username"]).exists():
                error = "Username already taken. Try Loging in!"
            
            # main show starts from here:
            # ===========================
            else:
                token = pyfunctions.generate_url()
                Temp_user.objects.create(uname=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], token=token)
                reciever = [request.POST["email"]]
                if pyfunctions.varification_mailto(reciever, token):
                    responce = "<h2> Email Sent <br /> Please Varify you email! </h2>"
                else:
                    responce = "<h1> ERROR! mail not sent </h1>" 
                return HttpResponse(responce)
            
            if error:
                return render(request, 'accounts/signup.html', {'title':'signup error', 'error':error})
        
        else: # request.method is "GET"
            return render(request, 'accounts/signup.html', {'title':'signup'})


def activate(request):
    path = str(request.path)
    key = path.split("validate/", 1)[1]
    error = ""

    if Temp_user.objects.filter(token=key).exists():
        tuser = Temp_user.objects.get(token=key)
        # Adding to user
        user = User.objects.create_user(tuser.uname, password=tuser.password, email=tuser.email)
        user.is_active = True

        # Deleting from Temp_user
        Temp_user.objects.filter(uname=tuser.uname).delete()
        return HttpResponse("<h1> Welcome to snapshare! </h1> <br />Thanks for varifying your email! try logging in! ")
    
    else:
        error = "This way does not lead to mars!"
    return HttpResponse(key + "<br /> <h1>" + error + "</h1>")