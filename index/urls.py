from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about),
    path('contacts', views.contacts),
]
