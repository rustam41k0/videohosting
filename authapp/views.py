from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    return render(request, 'logout.html')