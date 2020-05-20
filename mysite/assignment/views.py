from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth import login, authenticate

from .forms import UserForm, UserProfileForm

# Create your views here.

def index(request):
    return HttpResponse("Signup Successful")


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'form': user_form, 'form2': profile_form})


# @api_view(['POST','GET'])
# def login(request):
#     return render(request, 'login.html')