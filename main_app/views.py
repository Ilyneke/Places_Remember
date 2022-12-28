from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
# from .forms import MapModelForm
# from .models import Map


# class MapCreateView:
#     template_name = 'main_app/addmemory.html'
#     form_class = MapModelForm
#     success_message = 'Success: memory was created.'
#     success_url = reverse_lazy('main_app/index')
def addmem(request):
    return render(request, 'main_app/addmemory.html')


def index(request):
    return render(request, 'main_app/index.html')


def logout_view(request):
    logout(request)



