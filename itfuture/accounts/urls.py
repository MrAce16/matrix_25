from django.urls import path
from accounts import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
]
