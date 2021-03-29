from django.shortcuts import render

def Main(request):
    return render(request, 'main/home.html')


def Price(request):
    return render(request, 'main/price.html')


def Profile(request):
    return render(request, 'main/profil.html')


def AboutUs(request):
    return render(request, 'main/about us.html')


def Login(request):
    return render(request, 'main/login.html')


