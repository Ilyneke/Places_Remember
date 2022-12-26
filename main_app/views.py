from django.shortcuts import render


def index(request):
    return render(request, 'main_app/index.html')


def my_page(request):
    return render(request, 'main_app/mypage.html')
