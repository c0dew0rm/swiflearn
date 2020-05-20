from django.urls import path
from assignment import views
from django.conf.urls import url

urlpatterns = [
    path('index', views.index , name='index'),
    path('login/', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
]