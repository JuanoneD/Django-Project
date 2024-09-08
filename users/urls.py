from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path('InsertUser/',views.insertUser,name="insertUser"),
    path('loginUser',views.LoginUser,name='loginUser'),
]