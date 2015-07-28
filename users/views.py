from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def signin(request):
    context = {}
    post = request.POST
    if post:
        user = authenticate(
            username=post.get('email'),
            password=post.get('password'))

        # If the login was successful, go to the story list page
        if user:
            login(request, user)
            return redirect('list-stories')

        # If the login failed, put an error in the context
        context.update({'error': "Email/password combination incorrect!"})

    return render(request, 'signin.html', context)


@login_required(login_url=reverse_lazy('signin'))
def settings(request):
    context = {}
    return render(request, 'settings.html', context)


def signout(request):
    logout(request)
    return redirect('signin')
