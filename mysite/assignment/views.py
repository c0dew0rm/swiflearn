from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth import login, authenticate

from .forms import UserForm, UserProfileForm
from .models import UserProfile, ClassTaken, Class

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import UserProfileSerializer, ClassTakenSerializer, ClassSerializer
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
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username,password=password)
            login(request, user)
        except:
            HttpResponse("Invalid User Credentials")

        try:
            student = UserProfile.objects.get(user__username=username)
            if student is not None:
                url = "/details/"+str(student.id)
                return redirect(url)
            else:
                return HttpResponse("Student not found")
        except:
            Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return render(request, 'login.html')

@api_view(['GET'])
@permission_classes([AllowAny])
def details(request, pk):
    
    try:
        queryset = UserProfile.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    if request.method == 'GET':
        serializer_class = UserProfileSerializer(queryset)
        return Response(serializer_class.data)


class ClassTakenViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer