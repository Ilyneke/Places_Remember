from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.addmem, name='addmemory')
    # path('mypage', views.my_page),
]