from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main),
    path('price', views.Price),
    path('profile', views.Profile),
    path('about', views.AboutUs),
    path('login', views.Login),

]
