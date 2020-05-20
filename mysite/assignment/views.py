from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth import login, authenticate

from .forms import UserForm, UserProfileForm
from .models import UserProfile

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

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


@api_view(['POST','GET'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username,password=password)
            student = UserProfile.objects.get(user__username=username)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if student is not None:
            try:
                url = "details/"+str(student.id)
                return redirect(url)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return render("/")

    else:
        return render(request, 'login.html')