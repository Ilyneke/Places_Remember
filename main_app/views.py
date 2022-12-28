from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.views import View
from .models import Memory


# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         posts = Memory.objects.all()
#         return render(request, 'main_app/index.html', context={
#             'posts': posts
#         })


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"


def addmem(request):
    return render(request, 'main_app/addmemory.html')


def index(request):
    posts = Memory.objects.all()
    return render(request, 'main_app/index.html', {'posts': posts})


def logout_view(request):
    logout(request)



