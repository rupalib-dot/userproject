 
from django.contrib import admin
from django.urls import path
from userapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
]
