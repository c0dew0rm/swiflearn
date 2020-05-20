from django.urls import path, include
from assignment import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'classtaken', views.ClassTakenViewSet)

urlpatterns = [
    path('rest-api', include(router.urls)),
    path('index', views.index , name='index'),
    # url(r'^login/$', auth_views.LoginView, name='login'),
    # url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    path('details/<int:pk>/',views.details,name='details'),
]