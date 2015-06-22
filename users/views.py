from django.shortcuts import render


def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def signin(request):
    context = {}
    return render(request, 'signin.html', context)


def settings(request):
    context = {}
    return render(request, 'settings.html', context)
