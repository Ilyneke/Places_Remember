from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mypage', views.my_page),
]