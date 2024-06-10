from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def sign_in(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)            
            if user is not None:
                login(request, user)
                return redirect('dash:main')
    return render(request, 'dash/auth/sign-in.html')


@login_required
def update_profile(request):

    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username:
            user.username = username
        if password:
            user.set_password(password)

        user.save()
        login(request, user)
        return redirect('dash:main')

    return render(request, 'dash/auth/update.html', {'user':user})

@login_required
def sign_out(request):
    logout(request)
    return redirect('auth:sign-in')