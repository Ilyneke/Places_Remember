from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from .models import Memory
from .forms import MemoryForm


def addmem(request):
    return render(request, 'main_app/addmemory.html')


def index(request):
    form = MemoryForm()
    if not isinstance(request.user, AnonymousUser):  # если пользователь авторизован, возвращаем его воспоминания
        posts = Memory.objects.filter(author=request.user)
        return render(request, 'main_app/index.html', {'posts': posts, 'form': form})
    return render(request, 'main_app/index.html', {'form': form})  # иначе возвращаем без воспоминаний


def logout_view(request):
    logout(request)



