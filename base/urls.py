from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('grp/<str:gid>', views.group, name="group"),
]