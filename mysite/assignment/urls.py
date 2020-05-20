from django.urls import path
from assignment import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index', views.index , name='index'),
    # url(r'^login/$', auth_views.LoginView, name='login'),
    # url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
]