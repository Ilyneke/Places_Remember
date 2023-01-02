from django.shortcuts import render
from django.contrib.auth import logout, get_user
from django.contrib.auth.models import AnonymousUser
from .models import Memory
from .forms import MemoryForm


def addmem(request):
    return render(request, 'main_app/addmemory.html')


def view_map(request):
    return render(request, 'main_app/view_map.html')


def index(request):
    form_error = ''
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        form['author'].initial = get_user(request).pk
        print('form.data:', form.data)
        print('\nform.is_valid():', form.is_valid())
        if form.is_valid():
            form.save()
            form.clean()
        else:
            print('\nform.errors:', form.errors)
            form_error = 'Форма была заполнена неправильно!'
    else:
        form = MemoryForm()
    data = {
        'error': form_error,
        'form': form
    }
    if not isinstance(request.user, AnonymousUser):  # если пользователь авторизован, возвращаем его воспоминания
        posts = Memory.objects.filter(author=request.user)
        data['posts'] = posts
        return render(request, 'main_app/index.html', data)
    return render(request, 'main_app/index.html', data)  # иначе возвращаем без воспоминаний


def logout_view(request):
    logout(request)


