from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'snaps/index.html/')


# @login_required(login_url=reverse('login'))
# def upload(request):
#     if request.method == "POST":
#         pass
#     else:    
#         return render(request, 'snaps/upload.html/')


# @login_required(login_url=reverse('login'))
# def profile(request):
#     pass


# def albums(request):
#     if request.method == "POST":
#         pass
#     else: 
#         pass
