from django.urls import path
from assignment import views

urlpatterns = [
    path('index', views.index , name='index'),
    path('signUp/',views.signUp, name='signUp'),
    path('login/', views.login, name='login'),
]