from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.loginpage,name = "login"),
    path("logout/",views.logoutuser,name="logout"),
    path("register/",views.register,name="registration"),
    path("successful",views.succesful_registration),
]